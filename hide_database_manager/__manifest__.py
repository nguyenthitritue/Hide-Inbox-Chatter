# -*- coding: utf-8 -*-

{
    'name': "Hide database manager",
    'license': 'AGPL-3',
    'summary': """Hide link to database manager in login screen""",
    'description': """
        Hide link to database manager in login screen
    """,
    'version': "16.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'tools',
    'depends': ['base'],
    'price': 4.99,
    'currency': 'EUR',
    'data': [
        'views/common_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
