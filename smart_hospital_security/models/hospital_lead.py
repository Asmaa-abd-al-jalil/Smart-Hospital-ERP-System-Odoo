# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_blood_type = fields.Selection([
        ('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),
        ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')
    ], string="Blood Type")
    
    x_medical_allergies = fields.Text(string="Severe Allergies")

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # حقول مرتبطة (Read-only) لجلب البيانات من ملف المريض تلقائياً
    x_patient_blood_type = fields.Selection(related='partner_id.x_blood_type', string="Patient Blood Type", store=True)
    x_patient_allergies = fields.Text(related='partner_id.x_medical_allergies', string="Patient Allergies", store=True)