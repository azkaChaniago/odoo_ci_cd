# -*- coding: utf-8 -*-
# from odoo import http


# class Pilot(http.Controller):
#     @http.route('/pilot/pilot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pilot/pilot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pilot.listing', {
#             'root': '/pilot/pilot',
#             'objects': http.request.env['pilot.pilot'].search([]),
#         })

#     @http.route('/pilot/pilot/objects/<model("pilot.pilot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pilot.object', {
#             'object': obj
#         })
