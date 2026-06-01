# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Assigned Vehicle')

    @api.constrains('start', 'stop', 'partner_ids', 'vehicle_id')
    def _check_resource_availability(self):
        if self.env.context.get('install_mode'):
            return

        for event in self:
            if not event.start or not event.stop:
                continue
            
            if event.partner_ids:
                overlapping_doctors = self.env['calendar.event'].search([
                    ('id', '!=', event.id),          
                    ('start', '<', event.stop),      
                    ('stop', '>', event.start),      
                    ('partner_ids', 'in', event.partner_ids.ids), 
                    ('show_as', '=', 'busy')         
                ])
                if overlapping_doctors:
                    busy_partners = overlapping_doctors.mapped('partner_ids') & event.partner_ids
                    partner_names = ", ".join(busy_partners.mapped('name'))
                    raise ValidationError(_(
                        "Booking Conflict: (%s) is already busy during this time."
                    ) % partner_names)
            
            if event.vehicle_id:
                overlapping_vehicles = self.env['calendar.event'].search([
                    ('id', '!=', event.id),          
                    ('start', '<', event.stop),      
                    ('stop', '>', event.start),      
                    ('vehicle_id', '=', event.vehicle_id.id), 
                    ('show_as', '=', 'busy')         
                ])
                if overlapping_vehicles:
                    raise ValidationError(_(
                        "Vehicle Conflict: Vehicle (%s) is already deployed in another shift during this time."
                    ) % event.vehicle_id.name)