# Java Interface Protocol

从 Java 源码和已有协议整理接口文档的 Agent Skill。每个字段都有依据，声明、赋值和实际读取分别核对；嵌套对象按真实字段关系展开，未知信息明确保留。

An Agent Skill for evidence-based Java API documentation, with nested object tables and traceable field definitions. Instructions and examples are written in Chinese.

## 能做什么

- 从接口、Request、Response、DTO、父类和转换代码整理字段、泛型及对象关系。
- 对照已有协议核对类型、必填标注、参数来源和实现差异。
- 生成统一的四列表格，用合并表头、层级编号和浅色标记展示嵌套对象。
- 区分内部对象与外部依赖；源码不可见或协议存在冲突时，不补造结论。

本仓库提供给 AI 编码助手的说明文件，不是 Java 库、Maven 插件或自动解析器。使用 skill 本身不需要运行仓库中的 Python 校验脚本，也不需要特定 MCP 服务。

## 安装

### 使用 Skills CLI

需要 Node.js 22.20 或更新版本；这是当前 Skills CLI 的要求，不是 skill 本身的要求。

```bash
npx skills add https://github.com/xinsuoyusui687-commits/java-interface-protocol --skill java-interface-protocol
```

命令会让你选择安装到哪个编码助手。默认安装到当前项目；添加 `-g` 可安装到用户级别。也可以先查看可发现的 skill：

```bash
npx skills add https://github.com/xinsuoyusui687-commits/java-interface-protocol --list
```

### 在 Codex 中安装

向 Codex 提出：

```text
请使用 $skill-installer，从 GitHub 仓库 https://github.com/xinsuoyusui687-commits/java-interface-protocol 安装 skills/java-interface-protocol。
```

这是使用 Codex 自带安装技能的请求示例，需目标环境提供该安装技能。不要将安装器的本机脚本路径写死到共享文档。

### 手动安装

复制整个 `skills/java-interface-protocol/` 文件夹到目标助手支持的 skills 目录，保留 `references/`、`assets/` 和 `agents/`。具体扫描目录以该助手当前文档为准；不要只复制 `SKILL.md`。

本包遵循 Agent Skills 的目录和入口格式，并包含可选的 Codex 界面元数据。不同助手的自动发现和 HTML 渲染行为需要在实际环境确认；本次整理没有逐一验证所有助手。

## 使用

安装后，在支持该调用写法的助手中输入：

```text
请使用 $java-interface-protocol。
代码来源：<代码库绝对路径或已提供的源码包>
接口：com.example.api.OrderApi#queryOrder
已有协议：<可选，附上文件或正文>
输出位置：<指定目录或完整文件路径>
请保留真实 Java 类型，分别核对声明字段和实际使用字段，不补充没有依据的字段。
```

源码来源必填。未指定输出位置时，默认使用当前用户的实际桌面；无桌面的远程或服务端环境会先确认可写位置。一个 Java 接口的多个方法整理到同一份文档。

## 示例与显示效果

[完整示例](examples/README.md)包含虚构的 Java 源码和对应接口文档，展示嵌套对象、重复引用和必填标注。示例不包含真实业务数据。

协议正文使用 Markdown 标题和 HTML 表格。GitHub 可能移除内联样式，因此网页预览不保证显示底色与居中；对象名称、编号和文字引用仍可阅读。需要完整样式时，使用支持内联 HTML/CSS 的预览或导出工具。用户已有模板或目标格式有明确限制时，先按其要求处理。

## 仓库结构

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── docs/publishing.md
├── examples/
├── scripts/validate.py
├── requirements-dev.txt
├── .github/workflows/validate.yml
└── skills/java-interface-protocol/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    │   ├── evidence-rules.md
    │   ├── object-structure.md
    │   └── output-format.md
    └── assets/protocol-template.md
```

## 维护与发布

本地检查仅供维护者使用，需要 Python 3.10 或更新版本：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

GitHub Actions 会在推送和拉取请求时运行同一检查。检查通过表示文件结构、元数据、相对链接及演示表格符合本仓库约定，不代表已验证所有真实 Java 项目或助手的实际行为。

上传、安装验证和版本标签步骤见[发布说明](docs/publishing.md)；本次整理的变化见[变更记录](CHANGELOG.md)。

## 生成示例
<img width="723" height="864" alt="Snipaste_2026-11-27_15-03-55" src="https://github.com/user-attachments/assets/1655bc06-e3c8-4dec-bc5d-fea399f33c74" />

## 参考与许可

- [Agent Skills 规范](https://agentskills.io/specification)
- [OpenAI Skills 示例仓库](https://github.com/openai/skills)
- [Skills CLI](https://github.com/vercel-labs/skills)

沿用原 skill 声明的 MIT 许可，完整条款见 [LICENSE](LICENSE)。
