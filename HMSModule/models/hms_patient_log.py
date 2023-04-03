from odoo import models , fields

class HMSPatientLog(models.Model):

    _name = 'hms.patient.log'
    _rec_name = 'description'

    description = fields.Text()
    patient_id = fields.Many2one("hms.patient","log_id")
