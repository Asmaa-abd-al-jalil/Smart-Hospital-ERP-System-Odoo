# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import AccessError

@tagged('post_install', '-at_install', 'hospital_security')
class TestHospitalSecurityMatrix(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestHospitalSecurityMatrix, cls).setUpClass()
        cls.u_doctor = cls.env.ref('smart_hospital_security.user_doctor')
        cls.u_med_manager = cls.env.ref('smart_hospital_security.user_med_manager')
        cls.u_receptionist = cls.env.ref('smart_hospital_security.user_receptionist')
        cls.u_accountant = cls.env.ref('smart_hospital_security.user_accountant')

    def test_01_doctor_access_rights(self):
        """الطبيب: محظور من الحسابات والمشتريات"""
        doctor_env = self.env(user=self.u_doctor)
        with self.assertRaises(AccessError):
            doctor_env['account.move'].search([])
        with self.assertRaises(AccessError):
            doctor_env['purchase.order'].search([])

    def test_02_medical_manager_access_rights(self):
        """مدير العمليات: يرى الموظفين ومحظور من الحسابات"""
        manager_env = self.env(user=self.u_med_manager)
        try:
            manager_env['hr.employee'].search([])
        except AccessError:
            self.fail("خطأ: مدير العمليات محجوب عن الموظفين!")
        with self.assertRaises(AccessError):
            manager_env['account.move'].search([])

    def test_03_receptionist_invoice_creation(self):
        """موظف الاستقبال: مسموح له الفواتير"""
        receptionist_env = self.env(user=self.u_receptionist)
        try:
            receptionist_env['account.move'].search([])
        except AccessError:
            self.fail("خطأ: موظف الاستقبال محجوب عن الفواتير!")

    def test_04_accountant_access_restrictions(self):
        """المحاسب: مسموح له فواتير ومشتريات"""
        accountant_env = self.env(user=self.u_accountant)
        try:
            accountant_env['account.move'].search([])
            accountant_env['purchase.order'].search([])
        except AccessError:
            self.fail("خطأ: المحاسب تم حظره من الفواتير أو المشتريات!")