{
    'name': 'Bookstore Management',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Manage bookstore inventory and sales',
    'description': """
        This module provides functionality to manage:
        * Books
        * Authors
        * Publishers
        * Categories
        * Book Inventory
        * Sales Tracking
    """,
    'author': 'Abdulrahman Elsharef',
    'website': 'https://github.com/AbdulrahmanElsharef/Bookstore_Management_odoo',
    'depends': ['base', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/publisher_views.xml',
        'views/category_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}