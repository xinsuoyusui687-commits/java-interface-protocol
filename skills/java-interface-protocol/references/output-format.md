# 输出格式

用户明确提供模板时遵从其要求。以下是没有其他模板时的默认格式；原文中普通 Markdown 表格、单独“场景：”行与此规则不一致的示例不再沿用。

## 标题与内容

- 方法标题：`# 1. methodName -- 场景描述`；下一个方法为 `# 2. ...`。
- 方法标题下保留 `接口全路径：package.Interface#method`，场景已经放在标题中，不重复单列“场景：”。
- 请求为 `## 1.1. RequestType`，响应为 `## 1.2. ResponseType`；嵌套标题和编号按[对象层级规则](object-structure.md)递进。
- 对象名称保留真实 Java 名称，可在标题中附已有依据的中文说明；不得翻译成新的 Java 类名。
- 四列固定为“字段名称、字段类型、是否必填、说明”。字段说明填写业务含义、来源、格式、范围、默认值或使用条件，不重复必填依据或校验注解。
- Java 标识符、路径、枚举、日期格式可用行内代码；HTML 单元格中用 `<code>`，泛型尖括号必须转义。
- 没有依据的业务含义明确写“代码未声明”或具体未知情况，不从字段名称补造解释。
- 不自行增加与用户协议模板无关的分析章节。

## 合并表头与颜色

每个对象表首行合并四列并居中，第二行为四个列名；用 HTML 表格真实实现，不能用空的 Markdown 单元格模拟合并。

```html
<table>
  <tr><th colspan="4" style="text-align:center;background-color:#FFFFFF">Request</th></tr>
  <tr>
    <th style="background-color:#FFFFFF">字段名称</th>
    <th style="background-color:#FFFFFF">字段类型</th>
    <th style="background-color:#FFFFFF">是否必填</th>
    <th style="background-color:#FFFFFF">说明</th>
  </tr>
  <tr>
    <td style="background-color:#FFFFFF">fieldName</td>
    <td style="background-color:#FFFFFF">String</td>
    <td style="background-color:#FFFFFF">N</td>
    <td style="background-color:#FFFFFF">字段说明</td>
  </tr>
</table>
```

普通 `<th>`、`<td>` 白底 `#FFFFFF`。父表中的对象引用字段行与该子对象表首行使用相同浅色；为避免单元格白底遮住行色，直接为这些单元格设置对应背景色。重复引用行继续使用该对象颜色。颜色只辅助阅读，编号和文字引用必须独立可用。

### 既有对象配色

保留原 skill 的映射，遇到这些真实对象时使用；它们是格式约定，不是需要加入目标协议的类型清单。

| 对象简单名 | 背景色 |
| --- | --- |
| SupplierInfo | #FCE4EC |
| Segment | #E3F2FD |
| PassengerChangeInfo | #E8F5E9 |
| AirLineCondition | #FFF8E1 |
| StopInfo | #F3E5F5 |
| Cabin | #FFF3E0 |
| TicketInfo | #E0F7FA |
| TktSegment | #EDE7F6 |
| ChangeSearchResult | #ECEFF1 |
| ChangeChargeInfo | #E0F2F1 |
| PassengerCharge | #FFFDE7 |
| SupplierEngineInfo | #F1F8E9 |

其他对象分配未使用的浅色，并在本次文档中保持稳定。对象身份仍按完整类型和泛型实参判断；同名不同包时不能因简单名相同复用定义或颜色，可为后出现的对象分配另一颜色并用完整名区分。同一份文档中不同对象类型使用不同颜色。

## 渲染与检查

GitHub 等平台可能移除内联 `style`。保留 HTML 的真实合并结构，但不要声称 GitHub 网页一定显示颜色和居中；需要完整效果时使用支持内联 CSS 的渲染器。目标工具不支持 HTML 时，先说明影响并按用户决定调整格式。

交付前逐表检查四列、首行 `colspan="4"` 和居中；核对默认白底及对象引用与表头颜色一致。然后按真实对象树检查编号、引用和表数量。只有模板文件可以保留替换变量，正式生成的协议必须填入本案实际内容。
