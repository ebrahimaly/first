# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class product_point(models.Model):
    _name = 'product_point'

    name=fields.Many2one("product.template" ,string="Product",domain=[('sale_ok', '=', True)])
    start_date=fields.Date("Start Date")
    end_date=fields.Date("End Date")
    points=fields.Float(string="Points")
    status = fields.Selection([('draft', 'Draft'),
                             ('confirmed', "Confirmed"),
                             ('ended', 'Ended'),
                             ('cancelled', 'Cancelled')],default="draft", string="Status")

    last_change=fields.Many2one('res.users',string="Last Change",readonly="1")

    def set_confirm(self):
        self.status="confirmed"
        self.last_change=self.env.user

    # def __init__(self, name, age):
    #     for r in self:
    #         if r.end_date==datetime.now().date():
    #             r.status="ended"


    def set_cancel(self):
        self.status="cancelled"
        self.last_change=self.env.user

    # @api.onchange("end_date")
    # def check_time(self):
    #     if self.end_date==datetime.datetime.now():
    #         self.status="ended"


    def unlink(self):
        if self.env.user.has_group('product_point.group_delete_sale'):
            # raise ValidationError(_('You cannot .'))
            raise ValidationError(_('You cannot Delete recorde.'))

        return super(product_point, self).unlink()


class sale_point_line(models.Model):
    _inherit='sale.order.line'


    product_point=fields.Float("product point")




class sale_point(models.Model):
    _inherit="sale.order"

    total_point=fields.Float(string="Total Points",compute="_total_point")

    @api.depends("order_line")
    def _total_point(self):
        sum=0.0
        for r in self.order_line:
            sum+=r.product_point

        self.total_point=sum

    @api.onchange("order_line")
    def _get_point(self):
        for r in self:
            if r.order_line:
                for lm in r.order_line:
                    lm.product_point = self.env['product_point'].search([('name.name', '=', lm.product_id.name),
                                                                         ('status','=','confirmed')]).points*lm.product_uom_qty




