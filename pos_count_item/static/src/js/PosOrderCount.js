odoo.define("ilt_pos_item_count.PosCountOrderSummary", function (require) {
    "use strict";

    const OrderSummary = require("point_of_sale.OrderSummary");
    const Registries = require("point_of_sale.Registries");

    const PosCountOrderSummary = (OrderSummary) =>
        class PosCountOrderSummary extends OrderSummary {
            getCount() {
                return this.props.order.count_total_item();
            }
        };

    Registries.Component.extend(OrderSummary, PosCountOrderSummary);

    return PosCountOrderSummary;
});
