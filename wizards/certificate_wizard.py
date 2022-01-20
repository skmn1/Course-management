from odoo import api, models, fields
from datetime import datetime

class CertificateWizard(models.TransientModel):
    _name = 'course.certificate'

    

    @api.model
    def get_participants(self):
        session_id = self.env.context.get('active_id')
        session = self.env['course.session'].browse(session_id)
        return session.participant_list
 
    @api.multi
    def validate(self):
        session_id = self.env.context.get('active_id')
        session = self.env['course.session'].browse(session_id)
        for participant in self.participant_ids:
            self.env['course.certificate'].create({
                'date' : self.date,
                'description' : self.description,
                'participant_id' : participant.id,
                'course_id' : session.course.id,
                })

    date = fields.Date()
    description = fields.Text()
    participant_ids = fields.Many2many('course.participant', default=get_participants)
    course = fields.Many2one('course.course', string='course_id')
    



