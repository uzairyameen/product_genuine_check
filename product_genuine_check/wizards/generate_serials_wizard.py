from odoo import models, fields, api
from random import randint
from datetime import datetime
from odoo.exceptions import UserError  # Make sure to import UserError

class GenerateSerialsWizard(models.TransientModel):
    _name = 'generate.serials.wizard'
    _description = 'Generate Serial Numbers Wizard'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    amount = fields.Integer(string='Amount of Codes', required=True, default=1)

    def generate_serials(self):
        self.ensure_one()
        GenuineCheck = self.env['genuine.check']
        
        date_str = self.date.strftime('%d%m%y')
        product = self.product_id
        
        # Updated error message for missing serial code or packing code
        if not product.series_code or not product.packing_code:
            raise UserError('Product serial code and packing code are missing for the selected product.')
        
        prefix = f"{product.series_code}{product.packing_code}{date_str}"
        
        for _ in range(self.amount):
            serial = None
            attempts = 0
            while attempts < 99999:
                random_num = str(randint(1, 99999)).zfill(5)
                serial = f"{prefix}{random_num}"
                
                if not GenuineCheck.search_count([('serial', '=', serial)]):
                    break
                attempts += 1
            
            if attempts == 99999:
                raise UserError('No available serial numbers in the given range')
                
            GenuineCheck.create({
                'serial': serial,
                'product_id': product.id,
                'generation_date': self.date,
            })
            
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

