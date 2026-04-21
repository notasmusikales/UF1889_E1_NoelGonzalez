{
    'name': 'Seguimiento de Clientes',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Modulo para seguimiento de clientes',
    'description': 'Permite gestionar el seguimiento de clientes',
    'author': 'Noel Gonzalez',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/seguimiento_views.xml',
    ],
    'installable': True,
    'application': True,
}
