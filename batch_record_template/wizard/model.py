from odoo import models, fields, api


class Br(models.TransientModel):
    _name = "batches.request"


    name=fields.Char(string="Request No")
    date=fields.Date("Date")
    partner_id=fields.Many2one("res.users",string="From")
    to=fields.Char("To",default="Quality Assurance")
    product_id=fields.Many2one("product.product",string="Product Name")
    code=fields.Float("Product Code")
    size=fields.Char("Batch Size")
    batch_no=fields.Char("Batch Nos")
    ref=fields.Char("Reference Mrp No")
    market=fields.Char("Market")
    remark=fields.Text("Remark")

    request_by=fields.Many2one("res.users",string="Request By")
    create_date = fields.Date("sign & Date")
    received_by=fields.Many2one("res.users",string="Request Received By")
    received_date = fields.Date("sign & Date")

    remark_received=fields.Text(string="Remarks(If Any)")