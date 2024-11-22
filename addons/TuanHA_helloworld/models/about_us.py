from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    about_us = fields.Text(
        string="About Us",
        default="This is about company"
    )

    twitter_account = fields.Char(string="Twitter Account")
    facebook_account = fields.Char(string="Facebook Account")
    github_account = fields.Char(string="GitHub Account")
    linkedin_account = fields.Char(string="LinkedIn Account")
    youtube_account = fields.Char(string="YouTube Account")
    instagram_account = fields.Char(string="Instagram Account")
    tiktok_account = fields.Char(string="TikTok Account")

        
    # Các trường icon tương ứng
    twitter_icon = fields.Char(string="Twitter Icon")
    facebook_icon = fields.Char(string="Facebook Icon")
    github_icon = fields.Char(string="GitHub Icon")
    linkedin_icon = fields.Char(string="LinkedIn Icon")
    youtube_icon = fields.Char(string="YouTube Icon")
    instagram_icon = fields.Char(string="Instagram Icon")
    tiktok_icon = fields.Char(string="TikTok Icon")
