# -*- coding: utf-8 -*-
from odoo import models, fields, api

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

    @api.model_create_multi
    def create(self, vals_list):
        leads = super(CrmLead, self).create(vals_list)
        for lead in leads:
            # التحقق من الحالة عند الإنشاء إذا كانت "New Alert"
            if lead.stage_id and lead.stage_id.name == 'New Alert':
                lead._create_emergency_activity()
        return leads

    def write(self, vals):
        res = super(CrmLead, self).write(vals)
        if 'stage_id' in vals:
            for lead in self:
                # التحقق من الحالة عند التعديل
                if lead.stage_id and lead.stage_id.name == 'New Alert':
                    lead._create_emergency_activity()
        return res

    def _create_emergency_activity(self):
        self.ensure_one()
        # التأكد من عدم وجود نشاط مفتوح مسبقاً لهذا النوع لتجنب التكرار
        existing_activity = self.env['mail.activity'].search([
            ('res_model', '=', 'crm.lead'),
            ('res_id', '=', self.id),
            ('activity_type_id', '=', self.env.ref('smart_hospital_security.mail_activity_type_emergency').id)
        ])
        
        if not existing_activity:
            activity_type = self.env.ref('smart_hospital_security.mail_activity_type_emergency', raise_if_not_found=False)
            if activity_type:
                self.activity_schedule(
                    activity_type_id=activity_type.id,
                    summary='عاجل: تقييم حالة طارئة',
                    date_deadline=fields.Date.today(),
                )