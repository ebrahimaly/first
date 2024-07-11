from odoo import models, fields, api


class wizard_reason(models.TransientModel):
    _name="stage_reason"


    reason = fields.Text(string='Reason')