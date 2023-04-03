from odoo import models , fields


class HMSDoctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    Image = fields.Image()
    patient_id = fields.Many2many("hms.patient","doctor_id")