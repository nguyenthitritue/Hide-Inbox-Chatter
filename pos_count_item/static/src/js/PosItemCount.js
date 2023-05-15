odoo.define('pos_count.models', function (require) {
    "use strict";

    var { Order, Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');


    const PosOrderCount = (Order) => class PosOrderCount extends Order {
        count_total_item() {
            return this.orderlines.reduce((function(count, orderLine) {
                return count + orderLine.get_quantity();
            }), 0);
        }
    }
    Registries.Model.extend(Order, PosOrderCount);
});
