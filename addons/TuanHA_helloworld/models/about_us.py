from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    about_us = fields.Text(
        string="About Us",
        default="This is about company"
    )
