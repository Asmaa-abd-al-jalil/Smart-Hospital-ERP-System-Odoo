# -*- coding: utf-8 -*-
{
    'name': 'Smart Hospital Security & Access Control',
    'version': '1.0',
    'summary': 'Role-Based Access Control & Operations for Smart Mobile Hospital',
    'category': 'Custom',
    'author': 'Smart Hospital Team',
    'depends': [
        'base',
        'account',
        'hr',
        'stock',
        'purchase',
        'maintenance',
        'project',
        'fleet',
        

    ],
    'data': [
        'security/hospital_security_groups.xml',
        'security/ir.model.access.csv',
        'security/hospital_record_rules.xml',
        'users/hospital_users.xml', 
        'users/hospital_users_groups.xml',
        'users/hospital_employees.xml',
'fleet_logistics/inventory_locations.xml', 
        'fleet_logistics/fleet_vehicles.xml',
        'fleet_logistics/biomedical_assets.xml',
        'fleet_logistics/medical_products.xml',   
        'fleet_logistics/procurement_rules.xml',
        'fleet_logistics/maintenance_automation.xml',
        'data/automated_workflow.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}