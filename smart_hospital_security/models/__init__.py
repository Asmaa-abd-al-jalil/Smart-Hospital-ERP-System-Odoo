# -*- coding: utf-8 -*-
from . import fleet_logistics
from . import hospital_lead
from . import calendar_event
# def post_init_hook(cr, registry):
#     from odoo import api, SUPERUSER_ID
#     env = api.Environment(cr, SUPERUSER_ID, {})
    
#     product = env.ref('smart_hospital_security.product_epinephrine', raise_if_not_found=False)
#     if product:
#         product.write({
#             'tracking': 'lot',
#             'use_expiration_date': True
#         })

#     group_lot = env.ref('stock.group_production_lot', raise_if_not_found=False)
#     group_loc = env.ref('stock.group_stock_multi_locations', raise_if_not_found=False)
    
#     admin_user = env.ref('base.user_admin')
    
#     if group_lot:
#         group_lot.write({'users': [(4, admin_user.id)]})
#     if group_loc:
#         group_loc.write({'users': [(4, admin_user.id)]})