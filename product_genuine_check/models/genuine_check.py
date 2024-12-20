from odoo import models, fields, api
from random import randint
from datetime import datetime

class GenuineCheck(models.Model):
    _name = 'genuine.check'
    _description = 'Product Genuine Check'
    _rec_name = 'serial'

    serial = fields.Char(string='Serial Number', required=True, readonly=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    generation_date = fields.Date(string='Date of Generation', required=True)
    production_date = fields.Date(string='Date of Production')
    consumed = fields.Boolean(string='Consumed', default=False)
    consumption_date = fields.Date(string='Consumption Date')
    consumption_city = fields.Char(string='Consumption City')
    consumption_longitude = fields.Float(string='Consumption Longitude')
    consumption_latitude = fields.Float(string='Consumption Latitude')
    customer_id = fields.Many2one('res.partner', string='Customer')

    _sql_constraints = [
        ('serial_unique', 'unique(serial)', 'Serial number must be unique!')
    ]

