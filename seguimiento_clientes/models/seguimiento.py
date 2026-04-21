from odoo import models, fields


class Seguimiento(models.Model):
    _name = 'seguimiento.cliente'
    _description = 'Seguimiento de Clientes'

    name = fields.Char(string='Nombre', required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    date = fields.Date(string='Fecha', required=True, default=lambda self: fields.Date.today())
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('done', 'Realizado'),
    ], string='Estado', default='pending', required=True)
    notes = fields.Text(string='Notas')

    def action_done(self):
        self.state = 'done'