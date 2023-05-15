# -*- coding: utf-8 -*-
{
    'name': "Pos Count Item",
    'license': 'AGPL-3',
    'summary': """Count number item in POS""",
    'description': """
        Count number item in POS
    """,
    'version': "16.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'Sales/Point of Sale',
    'price': 4.99,
    'currency': 'USD',
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_count_item/static/src/css/item_count.scss',
            'pos_count_item/static/src/js/*',
            'pos_count_item/static/src/xml/*',
        ]
    },
}
