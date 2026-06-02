from odoo import models, fields, api, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # 1. تعريف الحقول أولاً!
    patient_heart_rate = fields.Integer(string="Patient Heart Rate")
    is_critical_iot_alert = fields.Boolean(string="Is Critical Alert", default=False)

    def write(self, vals):
        # 2. المنطق البرمجي
        if 'patient_heart_rate' in vals:
            heart_rate = vals['patient_heart_rate']
            
            if heart_rate < 40 or heart_rate > 140:
                vals['priority'] = '3' 
                vals['is_critical_iot_alert'] = True
                
                self.message_post(
                    body=_("SYSTEM OVERRIDE: CRITICAL VITALS DETECTED."),
                    message_type='notification',
                    subtype_xmlid='mail.mt_note'
                )
        
        return super(CrmLead, self).write(vals)