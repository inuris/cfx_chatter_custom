# -*- coding: utf-8 -*-
{
    'name': "CFX - Add Chatter to Modules",

    'summary': """
        CFX - Add Chatter to Modules""",

    'description': """
        CFX - Add Chatter to Modules
    """,

    'author': "KhoaLam",
    'website': "http://www.cofixel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],
    'data': [
        'views/account_view.xml',
        'views/product_views.xml',
        'views/uom_uom_views.xml'        
        ],
    # always loaded
    'installable': True,
    'application': True,
    'auto_install': False
}