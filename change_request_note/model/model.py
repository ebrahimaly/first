from odoo import api, fields, models

class changeRequestNote(models.Model):
    _name = "change.request"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('change.request')
        return super(changeRequestNote, self).create(vals)



    request_id=fields.Many2one('res.users',string="Initiated By")
    approve_id=fields.Many2one('res.partner',string="Approver By")

    create_date=fields.Date("Initiation Date")

    department_id=fields.Many2one("hr.department",string="Departments")

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "To Be Approved"),
            ("approved", "Approved"),
            ("done", "Done"),
            ("reject", "Rejected"),

        ],
        default="draft", string='state'
    )

    type = fields.Selection(
        [
            ("sop", "SOP"),
            ("mfc", "MFC"),
            ("mpc", "MPC"),
            ("spect", "specifications"),
            ("stp", "STP"),
            ("drawing", "Drawings"),
            ("mrp", "MRP(Manufacturing OR Packings)"),
            ("product", "products"),
            ("artwork", "Artwork"),
            ("facility", "Facility"),
            ("utility", "Utility"),
            ("equipment", "Equipment"),
            ("vendor", "Vendor"),
            ("material", "Material"),
            ("instrument", "Instrument"),
            ("gmp", "GMP Related Documents"),
            ("other", "Other"),

        ],
        default="sop", string='Change Type'
    )

    document=fields.Text(string="Document Title & Number")



    def action_approve(self):
        self.state="approved"


    def action_done(self):
            self.state="done"








