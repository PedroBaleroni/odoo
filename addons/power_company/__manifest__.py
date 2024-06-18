# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Power Companies',
    'category': 'Hidden',
    'description': """
Enable management of Power Companies: TUSD, price/kwh....
""",
    'version': '1.1',
    'depends': ['base'],
    'data': [
        'views/power_company_views.xml',
    ],
    'license': 'LGPL-3',
}
