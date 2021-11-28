# -*- coding: utf-8 -*-
from odoo import http

# class CourseManagementSystem(http.Controller):
#     @http.route('/course_management_system/course_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_management_system/course_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_management_system.listing', {
#             'root': '/course_management_system/course_management_system',
#             'objects': http.request.env['course_management_system.course_management_system'].search([]),
#         })

#     @http.route('/course_management_system/course_management_system/objects/<model("course_management_system.course_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_management_system.object', {
#             'object': obj
#         })