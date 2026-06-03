# -*- coding: utf-8 -*-
from odoo import models, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    def init(self):
        super(PosConfig, self).init()
        
        product_template = self.env.ref('smart_hospital_security.product_first_aid_kit', raise_if_not_found=False)
        location = self.env.ref('smart_hospital_security.location_mobile_unit_alpha', raise_if_not_found=False)
        
        if product_template and location:
            product_variant = product_template.product_variant_id
            
            existing_quant = self.env['stock.quant'].search([
                ('product_id', '=', product_variant.id),
                ('location_id', '=', location.id)
            ])
            
            if not existing_quant or sum(existing_quant.mapped('quantity')) == 0:
                quant = self.env['stock.quant'].with_context(inventory_mode=True).create({
                    'product_id': product_variant.id,
                    'location_id': location.id,
                    'inventory_quantity': 50.0,
                })
                quant.action_apply_inventory()

        pos_config = self.env.ref('smart_hospital_security.pos_config_truck_alpha', raise_if_not_found=False)
        payment_method = self.env.ref('smart_hospital_security.pos_payment_method_emergency', raise_if_not_found=False)
        
        if pos_config:
            if not pos_config.journal_id:
                sales_journal = self.env['account.journal'].search([
                    ('type', '=', 'sale'), 
                    ('company_id', '=', pos_config.company_id.id)
                ], limit=1)
                if sales_journal:
                    pos_config.write({'journal_id': sales_journal.id})

            if payment_method and not payment_method.journal_id:
                cash_journal = self.env['account.journal'].search([
                    ('type', 'in', ['cash', 'bank']), 
                    ('company_id', '=', pos_config.company_id.id)
                ], limit=1)
                if cash_journal:
                    payment_method.write({'journal_id': cash_journal.id})