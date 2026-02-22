{
    'name': 'Reporte de Tarea de Proyecto',
    'version': '17.0.1.0.0',
    'summary': 'Genera un reporte en PDF para cada tarea de proyecto con su descripción e imágenes adjuntas.',
    'author': 'Gemini',
    'website': 'https://gemini.google.com',
    'license': 'AGPL-3',
    'category': 'Project',
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/project_task_report_template.xml',
        'report/project_executive_report_template.xml',
        'wizard/project_executive_report_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
}
