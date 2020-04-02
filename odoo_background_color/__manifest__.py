# -*- coding: utf-8 -*-

{
    "name": "Odoo Background View",
    "summary": "Changing the background color",
    "version": "12.0.1.0.0",
    "category": "Theme/Backend",
    "website": "https://www.cybrosys.com",
    "description": """Backend theme for Odoo 12.0 """,
    'images': ['static/description/banner.jpg'],
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    "installable": True,
    "depends": ['base'],
    "data": [
        'views/background_view.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
