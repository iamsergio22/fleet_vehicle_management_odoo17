# -*- coding: utf-8 -*-
{
    'name': "Fleet Vehicle Mmanagement",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Sergio Rojas",
    'website': "https://www.yourcompany.com",
  
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [        
        'security/vehicle_security.xml',        
        'security/ir.model.access.csv',
        'views/vehicle_menu.xml',
        'views/vehicle_views.xml',
        'views/res_partner.xml',
        
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}

