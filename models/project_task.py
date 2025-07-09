from odoo import fields, models

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def _get_attached_images(self):
        """
        Busca y devuelve hasta 4 imágenes adjuntas a esta tarea.
        """
        self.ensure_one()
        return self.env['ir.attachment'].search([
            ('res_model', '=', 'project.task'),
            ('res_id', '=', self.id),
            ('mimetype', 'in', ['image/jpeg', 'image/png', 'image/gif']),
        ], limit=4)
