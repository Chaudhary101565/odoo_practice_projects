from odoo import models, fields, api


class MaintenanceTask(models.Model):
    _name = 'maintenance.task'
    _description = 'Maintenance Task'

    name = fields.Char(required=True)
    machine_id = fields.Many2one('product.product', domain=[('type', '=', 'service')], string="Machine")
    scheduled_date = fields.Date()
    assigned_to = fields.Many2one('res.users', string="Assigned To")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft')
    description = fields.Text()
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], default='medium')
    maintenance_type = fields.Selection([
        ('preventive', 'Preventive'),
        ('corrective', 'Corrective')
    ], default='preventive')
    completion_date = fields.Date()
    notes = fields.Text()

    def send_reminder(self):
        """Method to send reminder"""
        template = self.env.ref('maintenance_tracker.mail_template_maintenance_reminder')
        for task in self:
            if task.assigned_to and task.scheduled_date:
                template.send_mail(task.id, force_send=True)
