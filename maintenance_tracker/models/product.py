from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    last_maintenance_date = fields.Date(string="Last Maintenance Date", compute="_compute_last_maintenance_date",
                                        store=True)
    maintenance_task_ids = fields.One2many('maintenance.task', 'machine_id', string="Maintenance Tasks")

    @api.depends('maintenance_task_ids.completion_date')
    def _compute_last_maintenance_date(self):
        """Method to compute last maintenance date"""
        for product in self:
            product.last_maintenance_date = False
            last_date = self.env['maintenance.task'].search([
                ('machine_id', '=', product.id),
                ('state', '=', 'done')
            ], order='completion_date desc', limit=1).completion_date
            if last_date:
                product.last_maintenance_date = last_date
