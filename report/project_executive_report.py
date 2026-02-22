from odoo import models, api
from collections import defaultdict

class ProjectExecutiveReportTemplate(models.AbstractModel):
    _name = 'report.project_task_report.report_executive_template'
    _description = 'Reporte Ejecutivo de Proyectos'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data or not data.get('form'):
            return {}

        project_ids = data['form'].get('project_ids', [])
        tag_ids = data['form'].get('tag_ids', [])

        domain = [
            ('project_id', 'in', project_ids),
            ('parent_id', '=', False) # Only fetch parent tasks
        ]

        if tag_ids:
            domain.append(('tag_ids', 'in', tag_ids))

        tasks = self.env['project.task'].search(domain)
        
        grouped_data = defaultdict(lambda: defaultdict(list))

        for task in tasks:
            task_name = task.name
            project_name = task.project_id.name
            
            subtasks = task.child_ids

            if subtasks:
                for subtask in subtasks:
                   grouped_data[task_name][project_name].append(subtask)
            else:
                 if not grouped_data[task_name][project_name]:
                     grouped_data[task_name][project_name] = []

        return {
            'doc_ids': data.get('ids'),
            'doc_model': 'project.executive.report.wizard',
            'docs': self.env['project.executive.report.wizard'].browse(data.get('ids', [])),
            'grouped_data': dict(grouped_data),
        }
