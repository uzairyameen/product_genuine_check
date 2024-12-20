from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    series_code = fields.Char(string='Series Code', size=3, help='3-digit series code for genuine check')
    packing_code = fields.Char(string='Packing Code', size=3, help='3-digit packing code for genuine check')

    @api.constrains('series_code', 'packing_code')
    def _check_codes(self):
        for record in self:
            if record.series_code and (not record.series_code.isdigit() or len(record.series_code) != 3):
                raise ValidationError('Series Code must be exactly 3 digits')
            if record.packing_code and (not record.packing_code.isdigit() or len(record.packing_code) != 3):
                raise ValidationError('Packing Code must be exactly 3 digits')