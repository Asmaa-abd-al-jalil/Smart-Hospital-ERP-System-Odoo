from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    applicant_skill_ids = fields.Many2many(
        'hr.skill', 
        'hr_applicant_skill_rel', 
        'applicant_id', 
        'skill_id', 
        string="Clinical Skills"
    )