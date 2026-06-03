from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    medical_license_number = fields.Char(string='Medical License Number')
    license_expiry_date = fields.Date(string='License Expiry Date')