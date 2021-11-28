# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields, api


class Participant(models.Model):
    _name = 'course.participant'

    name = fields.Char(string='Name', Required = True)
    registration_nbr = fields.Integer(string='Registration number', Required = True)