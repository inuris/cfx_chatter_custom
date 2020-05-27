# -*- coding: utf-8 -*-
{
    'name': "CFX - Customized HR Leaves",

    'summary': """
        CFX - Customized HR Leaves""",

    'description': """
        CFX - Customized HR Leaves
    """,

    'author': "KhoaLam",
    'website': "http://www.cofixel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'calendar', 'resource', 'hr_holidays'],

    # always loaded
    'installable': True,
    'application': True,
    'auto_install': False
}