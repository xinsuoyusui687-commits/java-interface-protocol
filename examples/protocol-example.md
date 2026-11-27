# 1. queryOrder -- 按订单号查询订单

接口全路径：example.protocol.ExampleApi#queryOrder

## 1.1. QueryOrderRequest

<table>
  <tr><th colspan="4" style="text-align:center;background-color:#FFFFFF">QueryOrderRequest</th></tr>
  <tr><th style="background-color:#FFFFFF">字段名称</th><th style="background-color:#FFFFFF">字段类型</th><th style="background-color:#FFFFFF">是否必填</th><th style="background-color:#FFFFFF">说明</th></tr>
  <tr><td style="background-color:#FFFFFF">orderId</td><td style="background-color:#FFFFFF">String</td><td style="background-color:#FFFFFF">Y</td><td style="background-color:#FFFFFF">订单号</td></tr>
  <tr><td style="background-color:#E0E7FF">filter</td><td style="background-color:#E0E7FF">Filter</td><td style="background-color:#E0E7FF">N</td><td style="background-color:#E0E7FF">主筛选条件</td></tr>
  <tr><td style="background-color:#E0E7FF">alternateFilter</td><td style="background-color:#E0E7FF">Filter</td><td style="background-color:#E0E7FF">N</td><td style="background-color:#E0E7FF">备用筛选条件</td></tr>
</table>

备注：
　　● Filter定义详见1.1.1

### 1.1.1. Filter（筛选条件）

<table>
  <tr><th colspan="4" style="text-align:center;background-color:#E0E7FF">Filter</th></tr>
  <tr><th style="background-color:#FFFFFF">字段名称</th><th style="background-color:#FFFFFF">字段类型</th><th style="background-color:#FFFFFF">是否必填</th><th style="background-color:#FFFFFF">说明</th></tr>
  <tr><td style="background-color:#FFFFFF">statuses</td><td style="background-color:#FFFFFF">List&lt;String&gt;</td><td style="background-color:#FFFFFF">N</td><td style="background-color:#FFFFFF">允许的状态名称；取值范围在示例源码中未定义</td></tr>
</table>

## 1.2. QueryOrderResponse

<table>
  <tr><th colspan="4" style="text-align:center;background-color:#FFFFFF">QueryOrderResponse</th></tr>
  <tr><th style="background-color:#FFFFFF">字段名称</th><th style="background-color:#FFFFFF">字段类型</th><th style="background-color:#FFFFFF">是否必填</th><th style="background-color:#FFFFFF">说明</th></tr>
  <tr><td style="background-color:#DCFCE7">data</td><td style="background-color:#DCFCE7">OrderSummary</td><td style="background-color:#DCFCE7">N</td><td style="background-color:#DCFCE7">订单摘要</td></tr>
</table>

### 1.2.1. OrderSummary（订单摘要）

<table>
  <tr><th colspan="4" style="text-align:center;background-color:#DCFCE7">OrderSummary</th></tr>
  <tr><th style="background-color:#FFFFFF">字段名称</th><th style="background-color:#FFFFFF">字段类型</th><th style="background-color:#FFFFFF">是否必填</th><th style="background-color:#FFFFFF">说明</th></tr>
  <tr><td style="background-color:#FFFFFF">orderId</td><td style="background-color:#FFFFFF">String</td><td style="background-color:#FFFFFF">N</td><td style="background-color:#FFFFFF">订单号</td></tr>
  <tr><td style="background-color:#FFFFFF">status</td><td style="background-color:#FFFFFF">OrderStatus</td><td style="background-color:#FFFFFF">N</td><td style="background-color:#FFFFFF">订单状态：CREATED、CONFIRMED</td></tr>
</table>
