# -*- coding: utf-8 -*-
{
    'name': "Course management",

    'summary': """
       Easiest way for course management""",

    'description': """
        This module allows the management of the course centers, schools, etc.
    """,

    'author': "Soulimane KAMNI",
    'website': "https://www.linkedin.com/in/soulimane-kamni/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/course_view.xml',
        'views/participant_view.xml',
        'views/lecturer_view.xml',
        'views/session_view.xml',
        'views/classroom_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}