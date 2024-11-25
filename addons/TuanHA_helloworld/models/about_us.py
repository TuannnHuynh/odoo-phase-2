from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class ResCompany(models.Model):
    _inherit = "res.company"

    about_us = fields.Text(
        string="About Us",
        default="This is about company"
    )

    # Trường Account
    twitter_account = fields.Char(string="Twitter Account")
    facebook_account = fields.Char(string="Facebook Account")
    github_account = fields.Char(string="GitHub Account")
    linkedin_account = fields.Char(string="LinkedIn Account")
    youtube_account = fields.Char(string="YouTube Account")
    instagram_account = fields.Char(string="Instagram Account")
    tiktok_account = fields.Char(string="TikTok Account")
    zalo_account = fields.Char(string="Zalo Account")

    # Trường Icon
    twitter_icon = fields.Char(string="Twitter Icon")
    facebook_icon = fields.Char(string="Facebook Icon")
    github_icon = fields.Char(string="GitHub Icon")
    linkedin_icon = fields.Char(string="LinkedIn Icon")
    youtube_icon = fields.Char(string="YouTube Icon")
    instagram_icon = fields.Char(string="Instagram Icon")
    tiktok_icon = fields.Char(string="TikTok Icon")
    zalo_icon = fields.Char(string="Zalo Icon")

    @api.constrains(
        'twitter_icon', 'facebook_icon', 'github_icon', 'linkedin_icon',
        'youtube_icon', 'instagram_icon', 'tiktok_icon', 'zalo_icon'
    )
    def _check_icon_urls(self):
        """
        Kiểm tra định dạng URL hợp lệ cho các trường icon.
        """
        url_regex = re.compile(
            r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
        )
        for record in self:
            for field_name in [
                'twitter_icon', 'facebook_icon', 'github_icon', 'linkedin_icon',
                'youtube_icon', 'instagram_icon', 'tiktok_icon', 'zalo_icon'
            ]:
                field_value = getattr(record, field_name)
                if field_value and not url_regex.match(field_value):
                    raise ValidationError(f"Giá trị '{field_value}' trong trường {field_name.replace('_', ' ')} không phải là một URL hợp lệ.")

    @api.onchange(
        'twitter_icon', 'facebook_icon', 'github_icon', 'linkedin_icon',
        'youtube_icon', 'instagram_icon', 'tiktok_icon', 'zalo_icon'
    )
    def _onchange_icon_requires_account(self):
        """
        Đặt cảnh báo khi nhập icon mà chưa nhập account tương ứng.
        """
        account_fields = {
            'twitter_icon': 'twitter_account',
            'facebook_icon': 'facebook_account',
            'github_icon': 'github_account',
            'linkedin_icon': 'linkedin_account',
            'youtube_icon': 'youtube_account',
            'instagram_icon': 'instagram_account',
            'tiktok_icon': 'tiktok_account',
            'zalo_icon': 'zalo_account',
        }

        for icon_field, account_field in account_fields.items():
            icon_value = self[icon_field]
            account_value = self[account_field]
            if icon_value and not account_value:
                self[icon_field] = False  # Reset lại trường icon
                return {
                    'warning': {
                        'title': "Cảnh báo",
                        'message': f"Bạn phải nhập {account_field.replace('_', ' ')} trước khi nhập {icon_field.replace('_', ' ')}."
                    }
                }
