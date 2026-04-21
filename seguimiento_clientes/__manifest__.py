{
    'name': 'Seguimiento Clientes',
    'version': '1.0',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/seguimiento_views.xml',
    ],
    'installable': True,
    'application': True,
}