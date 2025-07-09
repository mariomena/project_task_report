from odoo import fields, models
from PIL import Image
import base64
import io

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

    def _get_rotated_image_b64(self, attachment):
        """
        Procesa un adjunto de imagen. Si es horizontal, la rota 90 grados.
        Devuelve la imagen procesada como una cadena base64.
        """
        self.ensure_one()
        if not attachment.datas:
            return None

        # Decodificar la imagen de base64
        image_data = base64.b64decode(attachment.datas)
        image_stream = io.BytesIO(image_data)
        
        try:
            img = Image.open(image_stream)
            width, height = img.size

            # Si la imagen es horizontal (width > height), rotarla
            if width > height:
                img = img.rotate(90, expand=True)
            
            # Guardar la imagen (rotada o no) en un buffer en memoria
            buffer = io.BytesIO()
            # Forzamos a PNG para evitar problemas de formato
            img.save(buffer, format='PNG')
            
            # Codificar la nueva imagen a base64 y devolverla
            return base64.b64encode(buffer.getvalue()).decode('utf-8')

        except Exception:
            # Si hay un error (ej. no es una imagen válida), devolver el original
            return attachment.datas.decode('utf-8')
