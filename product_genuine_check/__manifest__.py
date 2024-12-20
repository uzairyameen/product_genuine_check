{
    'name': 'Product Genuine Check',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Product genuineness verification system',
    'description': """
        This module adds product genuineness verification system with:
        - Serial codes generation
        - Genuine check tracking
        - Product verification
    """,
    'depends': [
        'base',
        'product',
        'stock',
        'sale_management',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/generate_serials_wizard_views.xml',
        'views/product_template_views.xml',
        'views/genuine_check_views.xml',
        
    ],
  
    'assets': {
        'web.assets_backend': [
            'product_genuine_check/static/src/js/generate_serials_button.js',
            'product_genuine_check/static/src/xml/generate_serials_button.xml',
               
        ],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': 1,
}