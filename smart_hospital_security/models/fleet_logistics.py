# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Host Mobile Hospital Unit')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    purchase_method = fields.Selection([
        ('purchase', 'On ordered quantities'),
        ('receive', 'On received quantities'),
    ], string='Control Policy', default='receive', required=True)

    @api.onchange('detailed_type')
    def _onchange_medical_product(self):
        if self.detailed_type == 'product':
            self.tracking = 'lot'
            self.use_expiration_date = True

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    x_storage_location_id = fields.Many2one('stock.location', string="Inventory Location")
    note = fields.Text(string="Notes")