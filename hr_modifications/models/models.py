# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class hr_recruitment(models.Model):
    _inherit="hr.applicant"


    @api.onchange("stage_id")
    def write_reason(self):
        print(123)
        self.ensure_one()
        return {
            'name': _('Reason'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'stage_reason',
            'target': 'new',
        }




