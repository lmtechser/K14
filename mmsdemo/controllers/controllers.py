# -*- coding: utf-8 -*-
from odoo import http


class Mmsdemo(http.Controller):
     @http.route('/mmsdemo/mmsdemo/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/mmsdemo/mmsdemo/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('mmsdemo.listing', {
             'root': '/mmsdemo/mmsdemo',
             'objects': http.request.env['mmsdemo.mmsdemo'].search([]),
         })

     @http.route('/mmsdemo/mmsdemo/objects/<model("mmsdemo.mmsdemo"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('mmsdemo.object', {
             'object': obj
         })
