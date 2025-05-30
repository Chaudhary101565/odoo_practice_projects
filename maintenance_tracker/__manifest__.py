{
    'name': 'Maintenance Tracker',
    'version': '18.0',
    'depends': ['base', 'mail', 'product', 'stock'],
    'author': 'Vishal Chaudhary',
    'category': 'Maintenance',
    'description': 'Track scheduled maintenance activities of machines/products.',
    'data': [
        'security/ir.model.access.csv',
        'security/maintenance_security.xml',
        'data/maintenance_mail_template.xml',
        'data/maintenance_cron.xml',
        'data/demo_data.xml',
        'views/maintenance_task_views.xml',
        'views/product_views.xml',
        'menu/menu.xml'
    ],
    'application': True,
    'assets': {
        'web.assets_backend_main': [
            'maintenance_tracker/static/src/css/maintenance_styles.css',
        ],
    },
}
