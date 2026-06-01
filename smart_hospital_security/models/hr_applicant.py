from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    skill_ids = fields.Many2many('hr.skill', string="Clinical Skills")