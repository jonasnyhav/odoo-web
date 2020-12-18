# -*- coding: utf-8 -*-
{
    'name': 'Alternative Dashboard',
    'version': '1.0',
    'category': 'Dashboard',
    'summary': 'Give 2 different views of dashboard base to use.',
    'description': """
            Alternative views for dashboard.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_views.xml',
        'views/assets.xml',
    ],
    # 'qweb': ['static/src/xml/board.xml'],
    'qweb': ['static/src/xml/js_widget_aden.xml'],
    'application': True,
}
