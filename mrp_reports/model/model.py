from odoo import api, fields, models


class productTemplate(models.Model):
    _inherit = "product.product"

    shelf_life=fields.Float("shelf Life")
    period_type = fields.Selection(
        [
            ("day", "Days"),
            ("weak", "Weeks"),
            ("month", "Months"),
            ("year", "Years"),

        ],
        default="day", string=' Type', required=True,
    )



class mrppro(models.Model):
    _inherit = "mrp.production"

    local=fields.Char("Market Local")
