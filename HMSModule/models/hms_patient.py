from odoo import models , fields , api

class HMSPatient(models.Model):

    _name = 'hms.patient'

    First_name = fields.Char()
    Last_name = fields.Char()
    Birth_date = fields.Date()
    History = fields.Html()
    CR_Ratio = fields.Float()
    Blood_type = fields.Selection ([('+a', '-a'),('+b', '-b'),('+c', '-c')])
    PCR = fields.Boolean()
    Image = fields.Image()
    Address = fields.Text()
    Age = fields.Integer()
    

    department_id = fields.Many2one('hms.department')
    doctor_id = fields.Many2many('hms.doctor')
