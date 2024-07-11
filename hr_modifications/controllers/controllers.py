# -*- coding: utf-8 -*-
# from odoo import http


# class HrModifications(http.Controller):
#     @http.route('/hr_modifications/hr_modifications/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_modifications/hr_modifications/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_modifications.listing', {
#             'root': '/hr_modifications/hr_modifications',
#             'objects': http.request.env['hr_modifications.hr_modifications'].search([]),
#         })

#     @http.route('/hr_modifications/hr_modifications/objects/<model("hr_modifications.hr_modifications"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_modifications.object', {
#             'object': obj
#         })
