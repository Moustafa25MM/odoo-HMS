from odoo import models , fields

class HMSPatientLog(models.Model):

    _name = 'hms.patient.log'
    _rec_name = 'description'


    created_by = fields.Many2one('users')
    date = fields.Date()
    description = fields.Char()
    log_id = fields.Many2one('hms.patient')
