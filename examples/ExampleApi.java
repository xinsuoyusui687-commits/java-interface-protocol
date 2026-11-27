package example.protocol;

import java.util.List;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;

/** 虚构的文档演示接口；不包含真实业务实现。 */
public interface ExampleApi {
    /** 按订单号查询订单。 */
    QueryOrderResponse queryOrder(QueryOrderRequest request);

    class QueryOrderRequest {
        /** 订单号。 */
        @NotBlank
        private String orderId;
        /** 主筛选条件。 */
        @Valid
        private Filter filter;
        /** 备用筛选条件。 */
        @Valid
        private Filter alternateFilter;
    }

    class Filter {
        /** 允许的状态名称；取值范围在此示例中未定义。 */
        private List<String> statuses;
    }

    class QueryOrderResponse {
        /** 订单摘要。 */
        private OrderSummary data;
    }

    class OrderSummary {
        /** 订单号。 */
        private String orderId;
        /** 订单状态。 */
        private OrderStatus status;
    }

    enum OrderStatus {
        CREATED, CONFIRMED
    }
}
