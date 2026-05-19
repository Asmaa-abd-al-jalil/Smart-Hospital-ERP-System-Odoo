# -*- coding: utf-8 -*-
{
    'name': 'Smart Hospital Security & Access Control',
    'version': '1.0',
    'summary': 'Role-Based Access Control (RBAC) for Smart Mobile Hospital',
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
    ],
    'data': [
        'security/hospital_security_groups.xml',
        'security/ir.model.access.csv',
        'security/hospital_record_rules.xml',
        'users/hospital_users.xml', 
        'users/hospital_users_groups.xml',
        'users/hospital_employees.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}