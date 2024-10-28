{
    'name': 'Todo App',
    'version': '1.0',
    'summary': 'todo_app_odoo tutorial',
    'sequence': -1,
    'description': """todo_app_odoo tutorial""",
    'category': 'todo_app_odoo',
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'todo_app_odoo/static/src/components/todo_list/todo_list.xml',
            'todo_app_odoo/static/src/components/todo_list/todo_list.js',
            'todo_app_odoo/static/src/components/todo_list/todo_list.scss'
        ],

    },
}
