# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'course.course'


    name = fields.Char(string='Name', required = True)
    category = fields.Char(string='category')
    price = fields.Float(string='Price', digits=(12, 2))
    description = fields.Text()
    session_list = fields.One2many('course.session','course', string='Sessions')


# class Lecturer(models.Model):
#     _name = 'course.lecturer'
#     _inherit = 'res.users'

#     name = fields.Char(string='Name', required = True)
#     id_number = fields.Integer(string='Identification number', required = True)
#     degree = fields.Char(string='Degree')

#     _sql_constraints = [('id_number_unique', 'unique(id_number)', 'Indetification number must be unique')]

class Session(models.Model):
    _name = 'course.session'

    name = fields.Char(string='Name', required = True)
    nbr_participant = fields.Integer(string='Participants number')
    starting_date = fields.Date(string='Starting date')
    end_date = fields.Date(string='End date')
    status = fields.Selection([('a', 'active'), ('u', 'unactive')], string='Status')
    lecturer_ids = fields.Many2many('course.lecturer', string='Lecturers')
    course = fields.Many2one('course.course', string='Course')
    participant_list = fields.Many2many('course.participant', string='Participants')
    classroom_list = fields.Many2many('course.classroom', string='Classrooms')

    ###  constrains ###
    @api.constrains('starting_date','end_date')
    def check_dates(self) :
        if self.end_date < self.starting_date :
            raise ValidationError('End date must be greater than starting date')

    
class Lecturer(models.Model):
    _name = 'course.lecturer'
    _inherits = {'res.users':'lecturer_id'}

    lecturer_id = fields.Many2one('res.users', required=True, ondelete='restrict', auto_join=True,
    string='Related user', help='User-related data of the lecturer')
    session_ids = fields.Many2many('course.session', string='Sessions')
    about = fields.Text('about')

class Classroom(models.Model):
    _name = 'course.classroom'
    
    name = fields.Char(string='Name', required = True)
    seats_nbr = fields.Integer(string='Seats number', required = True, default= 25 )
    booked = fields.Boolean(string='Booked', required = True)
    session_list = fields.Many2many('course.session', string='Sessions')

class Participant(models.Model):
    _name = 'course.participant'

    name = fields.Char(string='Name', required = True)
    registration_nbr = fields.Integer(string='Registration number', required = True)
    session_list = fields.Many2many('course.session', string='Sessions')

    _sql_constraints = [('registration_nbr_unique', 'unique(registration_nbr)', 'Registration number must be unique')]
# # @api.depends('value')
# # def _value_pc(self):
# #     self.value2 = float(self.value) / 100

class Certificate(models.Model):
    _name = 'course.certificate'
    _rec_name = 'participant'

    name = fields.Char(string='Certificate')
    date = fields.Date()
    description = fields.Text()
    participant = fields.Many2one('course.participant', string='participant')
    course = fields.Many2one('course.course', string='course')   
 