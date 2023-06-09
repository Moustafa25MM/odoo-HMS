from odoo import models , fields , api
from datetime import date
from odoo.exceptions import ValidationError

class HMSPatient(models.Model):

    _name = 'hms.patient'

    First_name = fields.Char()
    Last_name = fields.Char()
    Birth_date = fields.Date(string ="Date_of_birth")
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
    Age = fields.Integer(string= "myAge" , compute="compute_age")
    email = fields.Char(string="Email")
    

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

    @api.onchange('State')
    def state_change(self):
        values = {
            #'created_by': self.doctor_id,
            'date': date.today(),
            'description' : f'State Changed to {self.State}',
            #'log_id' : self._ids
        }
        log = self.env['hms.patient.log'].create(values)
        self.patient_logs += log

     
    def set_Undetermined(self):
        self.State = 'undetermined'
    
    def set_Good(self):
        self.State = 'good'

    def set_Fair(self):
        self.State = 'fair'
    
    def set_Serious(self):
        self.State ='serious'


    
    @api.onchange('Age')
    def onChange_Age(self):
        if self.Age > 30 :
            self.PCR = True
            return {
                'warning': {
                    'message': 'PCR has been changed'   
                }
            }

    
    _sql_constraints = [
        ('Duplicate_Email', 'unique (Email)', 'Email address already exists!')
    ]


    @api.depends('Birth_date')
    def compute_age(self):
        for rec in self :
            if rec.Birth_date:
                today = date.today()
                rec.Age = today.year - rec.Birth_date.year - (
                    (today.month, today.day) < (rec.Birth_date.month, rec.Birth_date.day)
                )
            else :
                rec.Age = 0 