# -*- coding: utf-8 -*-
# from odoo import http


# class TestFleetVehicleManagement(http.Controller):
#     @http.route('/test_fleet_vehicle_management/test_fleet_vehicle_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_fleet_vehicle_management/test_fleet_vehicle_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_fleet_vehicle_management.listing', {
#             'root': '/test_fleet_vehicle_management/test_fleet_vehicle_management',
#             'objects': http.request.env['test_fleet_vehicle_management.test_fleet_vehicle_management'].search([]),
#         })

#     @http.route('/test_fleet_vehicle_management/test_fleet_vehicle_management/objects/<model("test_fleet_vehicle_management.test_fleet_vehicle_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_fleet_vehicle_management.object', {
#             'object': obj
#         })

