#!/usr/bin/env python3
"""Validate this repository's skill metadata, local links and example tables."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'java-interface-protocol'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_frontmatter():
    content = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', content, re.S)
    require(match, 'SKILL.md must start with YAML frontmatter')
    meta = yaml.safe_load(match.group(1))
    require(isinstance(meta, dict), 'Frontmatter must be a mapping')
    allowed = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
    require(not (set(meta) - allowed), 'Unsupported top-level metadata field')
    name = meta.get('name', '')
    require(isinstance(name, str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name), 'Invalid skill name')
    require(len(name) <= 64 and name == SKILL.name, 'Skill name and directory must match')
    description = meta.get('description', '')
    require(isinstance(description, str) and 1 <= len(description) <= 1024, 'Invalid description')
    metadata = meta.get('metadata', {})
    require(isinstance(metadata, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()), 'metadata must be a string-to-string map')
    require(meta.get('license') == 'MIT' and (ROOT / 'LICENSE').is_file(), 'MIT license file is missing')
    require(len(content[match.end():].splitlines()) < 500, 'Entrypoint should remain concise')
    ui = yaml.safe_load((SKILL / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
    interface = ui.get('interface', {})
    require(all(isinstance(interface.get(k), str) and interface[k] for k in ('display_name', 'short_description', 'default_prompt')), 'Missing UI strings')
    require(25 <= len(interface['short_description']) <= 64, 'UI short description must be 25-64 characters')
    require('$' + name in interface['default_prompt'], 'Default prompt must invoke the skill')
    version = metadata.get('version', '')
    require(re.fullmatch(r'\d+\.\d+\.\d+', version), 'Expected semantic version')
    require(version in (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8'), 'Version is absent from CHANGELOG')


def validate_links_and_text():
    count = 0
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding='utf-8')
        require('\ufffd' not in text and not text.startswith('\ufeff'), f'Invalid encoding: {path.relative_to(ROOT)}')
        if path.suffix == '.md':
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', text):
                target = target.strip().strip('<>')
                uri = urlsplit(target)
                if uri.scheme or target.startswith('#'):
                    continue
                resolved = (path.parent / unquote(uri.path)).resolve()
                require(resolved.is_relative_to(ROOT.resolve()), f'Link leaves repository: {path.name}: {target}')
                require(resolved.exists(), f'Broken local link: {path.name}: {target}')
                count += 1
    return count


class Tables(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.rows = None
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            require(self.rows is None, 'Nested HTML tables are unsupported in the example')
            self.rows = []
        elif tag == 'tr' and self.rows is not None:
            self.row = []
        elif tag in ('th', 'td') and self.row is not None:
            self.cell = {'tag': tag, 'attrs': dict(attrs), 'text': ''}

    def handle_data(self, data):
        if self.cell is not None:
            self.cell['text'] += data

    def handle_endtag(self, tag):
        if tag in ('th', 'td') and self.cell is not None:
            self.row.append(self.cell)
            self.cell = None
        elif tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None
        elif tag == 'table' and self.rows is not None:
            self.tables.append(self.rows)
            self.rows = None


def background(cell):
    match = re.search(r'background-color\s*:\s*(#[0-9a-fA-F]{6})', cell['attrs'].get('style', ''))
    require(match, 'Every example table cell needs an explicit background')
    return match.group(1).upper()


def validate_example():
    parser = Tables()
    text = (ROOT / 'examples' / 'protocol-example.md').read_text(encoding='utf-8')
    parser.feed(text)
    names = []
    tables = {}
    for rows in parser.tables:
        require(len(rows) >= 3 and len(rows[0]) == 1, 'Missing object heading')
        first = rows[0][0]
        require(first['tag'] == 'th' and first['attrs'].get('colspan') == '4', 'Object heading must span four columns')
        require('text-align:center' in first['attrs'].get('style', '').replace(' ', ''), 'Object heading must be centered')
        name = first['text'].strip()
        names.append(name)
        tables[name] = rows
        require([c['text'] for c in rows[1]] == ['字段名称', '字段类型', '是否必填', '说明'], 'Invalid column labels')
        require(all(background(c) == '#FFFFFF' for c in rows[1]), 'Column headers must be white')
        for row in rows[2:]:
            require(len(row) == 4 and all(c['tag'] == 'td' for c in row), 'Field row must have four cells')
            require(len({background(c) for c in row}) == 1, 'A field row must use one background')
    expected = ['QueryOrderRequest', 'Filter', 'QueryOrderResponse', 'OrderSummary']
    require(names == expected, 'Example object definitions are missing or duplicated')
    require('List<String>' == tables['Filter'][2][1]['text'], 'Generic type was not preserved')
    require(tables['QueryOrderRequest'][2][2]['text'] == 'Y', 'NotBlank field must be Y in this example')
    for row in tables['QueryOrderRequest'][3:]:
        require(row[2]['text'] == 'N', 'Valid alone must not make the object required')
        require(background(row[0]) == background(tables['Filter'][0][0]) != '#FFFFFF', 'Filter colors must match')
    require(background(tables['QueryOrderResponse'][2][0]) == background(tables['OrderSummary'][0][0]) != '#FFFFFF', 'Summary colors must match')
    require(background(tables['Filter'][0][0]) != background(tables['OrderSummary'][0][0]), 'Distinct objects need distinct colors')
    headings = set(re.findall(r'^#{1,6}\s+([0-9]+(?:\.[0-9]+)*)\.', text, re.M))
    for ref in re.findall(r'定义详见([0-9]+(?:\.[0-9]+)*)', text):
        require(ref in headings, 'Example reference has no matching heading')
    require('### 1.1.1. Filter' in text and '### 1.2.1. OrderSummary' in text, 'Incorrect example nesting')
    return len(names)


def main():
    try:
        validate_frontmatter()
        links = validate_links_and_text()
        objects = validate_example()
        yaml.safe_load((ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8'))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: skill metadata, UI metadata, version, UTF-8, {links} local links, {objects} example objects and workflow YAML')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
