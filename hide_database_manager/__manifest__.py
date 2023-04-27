# -*- coding: utf-8 -*-

{
    'name': "Hide database manager",
    'license': 'AGPL-3',
    'summary': """Hide link to database manager in login screen""",
    'description': """
        Hide link to database manager in login screen
    """,
    'version': "14.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'tools',
    'depends': ['base'],
    'price': 1.99,
    'currency': 'USD',
    'data': [
        'views/common_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
