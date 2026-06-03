from odoo import models, fields, api, _

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    patient_heart_rate = fields.Integer(string="Patient Heart Rate")
    is_critical_iot_alert = fields.Boolean(string="Is Critical Alert", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self._check_critical_vitals(vals)
        return super().create(vals_list)

    def write(self, vals):
        self._check_critical_vitals(vals)
        return super().write(vals)

    def _check_critical_vitals(self, vals):
        if 'patient_heart_rate' in vals:
            heart_rate = vals['patient_heart_rate']
            
            if heart_rate < 40 or heart_rate > 140:
                vals.update({
                    'priority': '3',
                    'is_critical_iot_alert': True
                })
                self.sudo().message_post(
                    body=_("SYSTEM OVERRIDE: CRITICAL VITALS DETECTED."),
                    message_type='notification',
                    subtype_xmlid='mail.mt_note'
                )
            
            else:
                vals.update({
                    'priority': '0', 
                    'is_critical_iot_alert': False
                })