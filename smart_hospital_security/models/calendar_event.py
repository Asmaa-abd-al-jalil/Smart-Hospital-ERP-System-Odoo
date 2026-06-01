# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.constrains('start', 'stop', 'partner_ids')
    def _check_doctor_availability(self):
        if self.env.context.get('install_mode'):
            return

        for event in self:
            if not event.start or not event.stop or not event.partner_ids:
                continue
            
            overlapping_events = self.env['calendar.event'].search([
                ('id', '!=', event.id),         
                ('start', '<', event.stop),     
                ('stop', '>', event.start),   
                ('partner_ids', 'in', event.partner_ids.ids), 
                ('show_as', '=', 'busy')       
            ])
            
            if overlapping_events:
                busy_partners = overlapping_events.mapped('partner_ids') & event.partner_ids
                partner_names = ", ".join(busy_partners.mapped('name'))
                
                raise ValidationError(_(
                    "🚨 [منظومة Lifeline Sync - تعارض في جدولة الموارد الطبية]\n\n"
                    "خطأ: لا يمكن إتمام الحجز! المورد أو الطبيب الميداني المختار (%s) "
                    "مشغول حالياً بمناوبة طوارئ مكثفة أو حجز أصول متعارض خلال هذه الفترة الزمنية.\n\n"
                    "💡 الإجراء المطلوب:\n"
                    "يرجى مراجعة لوحة الحجب البصري (Visual Calendar View) لتفادي الحجز المزدوج واختيار وقت متاح."
                ) % partner_names)  