# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class PowerCompany(models.Model):
    _name = 'power.company'
    _description = 'Power Company'
    
    name = fields.Char(string='Name', required=True)
    kwh_price = fields.Float(string='Price/kWh', required=True)
    tusd_price = fields.Float(string='TUSD', required=True)
    taxes = fields.Float(string='Taxes', required=False)
    
    _sql_constraints = [
        ('unique_id', 'UNIQUE(id)', 'The id must be unique'),
    ]
    
    @api.model_create_multi
    def create(self, vals_list):
        new_ids = self.env['power.company']._get_unique_ids([vals.get('id') for vals in vals_list])
        for vals, new_id in zip(vals_list, new_ids):
            vals['id'] = new_id
        return super().create(vals_list)
    
    def write(self, vals):
        return super().write(vals)
    
    def copy(self, default=None):
        return super().copy(default)