from odoo import models , fields , api
from datetime import date


class HMSPatient(models.Model):

    _name = 'hms.patient'

    First_name = fields.Char()
    Last_name = fields.Char()
    Birth_date = fields.Date()
    History = fields.Html()
    CR_Ratio = fields.Float()
    Blood_type = fields.Selection ([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-')
        ])
    PCR = fields.Boolean()
    Image = fields.Image()
    Address = fields.Text()
    Age = fields.Integer()
    

    department_id = fields.Many2one('hms.department')
    department_capacity = fields.Integer(related="department_id.department_capacity")
    doctor_id = fields.Many2many('hms.doctor')

    State = fields.Selection([
        ('undetermined','Undetermined'),
        ('good','Good'),
        ('fair','Fair'),
        ('serious','Serious')
    ])

    patient_logs = fields.One2many('hms.patient.log','log_id')

    @api.onchange('state')
    def state_change(self):
        values = {
            'created_by': self.uid,
            'date': date.today(),
            'description' : f'State Changed to {self.state}',
            'log_id' : self.id
        }
        log = self.env['hms.patient.log'].create(values)
        self.patient_logs += log

     
    def set_Undetermined(self):
        self.state = 'undetermined'
    
    def set_Good(self):
        self.state = 'good'

    def set_Fair(self):
        self.state = 'fair'
    
    def set_Serious(self):
        self.state ='serious'