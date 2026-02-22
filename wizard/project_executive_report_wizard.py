from odoo import models, fields, api

class ProjectExecutiveReportWizard(models.TransientModel):
    _name = 'project.executive.report.wizard'
    _description = 'Wizard for Executive Project Report'

    project_ids = fields.Many2many('project.project', string='Proyectos', required=True)
    tag_ids = fields.Many2many('project.tags', string='Etiquetas (Mes/Año)')

    def action_generate_report(self):
        self.ensure_one()
        data = {
            'form': self.read()[0],
        }
        return self.env.ref('project_task_report.action_report_project_executive').report_action(self, data=data)
