# -*- coding: utf-8 -*-
# from odoo import http


# class ProductPoint(http.Controller):
#     @http.route('/product_point/product_point/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_point/product_point/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_point.listing', {
#             'root': '/product_point/product_point',
#             'objects': http.request.env['product_point.product_point'].search([]),
#         })

#     @http.route('/product_point/product_point/objects/<model("product_point.product_point"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_point.object', {
#             'object': obj
#         })
