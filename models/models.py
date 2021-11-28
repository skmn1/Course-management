# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course_management_system(models.Model):
    _name = 'course_management_system.course_management_system'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100



class Course(models.Model):
    _name = 'course.course'


    name = fields.Char(string='Name', Required = True)
    category = fields.Char(string='category')
    price = fields.Float(string='Price', digits=(12, 2))
    description = fields.Text()
    session_list = fields.One2many('course.session','course', string='Sessions')


class Lecturer(models.Model):
    _name = 'course.lecturer'

    name = fields.Char(string='Name', required = True)
    degree = fields.Char(string='Degree')

class Session(models.Model):
    _name = 'course.session'

    name = fields.Char(string='Name', Required = True)
    nbr_participant = fields.Integer(string='Participants number')
    starting_date = fields.Date(string='Starting date')
    end_date = fields.Date(string='End date')
    status = fields.Selection([('a', 'active'), ('u', 'unactive')], string='Status')
    lecturer_list = fields.Many2many('course.lecturer', string='Lecturers')
    course = fields.Many2one('course.course', string='Course')


class Classroom(models.Model):
    _name = 'course.classroom'
    
    name = fields.Char(string='Name', Required = True)
    seats_nbr = fields.Integer(string='Seats number', Required = True)
    booked = fields.Boolean(string='Booked', Required = True)

# # @api.depends('value')
# # def _value_pc(self):
# #     self.value2 = float(self.value) / 100