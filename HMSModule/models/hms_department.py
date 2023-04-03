from odoo import models , fields


class HMSDepartment(models.Model):

    _name = 'hms.department'
    _rec_name = 'department_name'
    department_name = fields.Char()
    department_capacity = fields.Integer()
    isOpened = fields.Boolean()
    patients = fields.Char()
    patient_id = fields.One2many("hms.patient","department_id")