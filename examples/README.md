# 虚构示例

[ExampleApi.java](ExampleApi.java)与[对应接口文档](protocol-example.md)是一组自包含的格式演示。源码没有真实服务调用，未承诺接口可运行；文档描述类声明，不声称字段已被实际赋值或读取。

Request/Response、Filter、OrderSummary 的完整类型均位于 `example.protocol.ExampleApi` 内，不能用简单类名到真实项目中替换。

- `orderId` 的 `Y` 来自字段上的 `@NotBlank`。
- `filter` 和 `alternateFilter` 只有 `@Valid`，不因此标必填。
- `Filter` 只展开一次，第二处引用指向首次定义；两处引用与定义表头同色。
- `data` 的 OrderSummary 是响应的直接子对象，编号为 `1.2.1.`。
- `List<String>` 和枚举名保留原类型。枚举值来自源码，筛选状态范围未定义则明确说明。

示例使用 Jakarta Validation 的真实注解名称；如单独编译 Java 文件，需要相应 API 依赖。运行本仓库的文档检查无需编译 Java 或下载 Java 依赖。
