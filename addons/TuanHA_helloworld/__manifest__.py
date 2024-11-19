{
    # Tên module
    'name': 'Tutorial Odoo 17.0',
    'version': '1.0',

    # Loại module
    'category': 'Tutorial',

    'sequence': 5,

    'summary': 'Module xây dựng khoá học lập trình',
    'description': '',

    'depends': ["base","website"],

    'installable': True,
    'auto_install': False,
    'application': True,

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/about.xml',
        'views/modal.xml',
        'views/snippets.xml',
        'views/course_list_template.xml',
        'views/menu_item_course.xml',
        'views/menu_item_lesson.xml',
        'views/menu_view.xml',
    ],
    'assets': {
        'web.assets_frontend':[
            "web/static/src/libs/fontawesome/css/font-awesome.css",
        ],
        'point_of_sale._assets_pos': [
            'TuanHA_helloworld/static/src/**/*'
        ],

    },
    'license': 'LGPL-3',
}
