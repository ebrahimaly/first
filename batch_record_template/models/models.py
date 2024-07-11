# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError, UserError



class batch_record_template(models.Model):

    _inherit="mrp.production"

    is_approve=fields.Boolean(copy=False)

    confirm=fields.Boolean(compute="show_button_confirm")

    def show_button_confirm(self):
        for rec in self:
            if rec.state=='draft' and rec.is_approve==True:
                rec.confirm=True
            else:
                rec.confirm=False

    def manger_approve(self):
        self.is_approve=True



    def generate_br(self):
        self.ensure_one()
        return {
            'name': _('Generate BR'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'batches.request',
            'target': 'new',
        }


