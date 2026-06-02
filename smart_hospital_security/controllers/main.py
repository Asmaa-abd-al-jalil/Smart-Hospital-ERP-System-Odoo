from odoo import http
from odoo.http import request

class HospitalIoTController(http.Controller):

    @http.route('/api/hospital/vitals/update', type='json', auth='public', methods=['POST'], csrf=False)
    def update_vitals(self, ticket_id=None, heart_rate=None):
        if not ticket_id or heart_rate is None:
            return {'status': 'error', 'message': 'Missing parameters'}

        lead = request.env['crm.lead'].sudo().browse(ticket_id)

        if not lead.exists():
            return {'status': 'error', 'message': 'Ticket not found'}

        try:
            lead.write({'patient_heart_rate': heart_rate})
            return {'status': 'success', 'message': f'Heart rate updated for {ticket_id}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}