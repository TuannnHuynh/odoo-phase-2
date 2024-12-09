from odoo import http
from odoo.http import request,Response
import json

class WebsiteAbout(http.Controller):
    
    @http.route('/about_us', type='http', auth='public', website=True, methods=['GET'])
    def get_about_data(self):
        """
        API trả về dữ liệu "About Us" và các tài khoản mạng xã hội của tất cả các công ty.
        """
        companies = request.env['res.company'].sudo().search([])  # Lấy tất cả các công ty
        if not companies:
            return Response(json.dumps({'error': 'No company found'}), content_type='application/json', status=404)

        # Chuẩn bị danh sách dữ liệu của tất cả công ty
        data = []
        for company in companies:
            company_data = {
                "about_us": company.about_us or "About Us content not available.",
                "social_accounts": {
                    "twitter": company.twitter_account or "",
                    "facebook": company.facebook_account or "",
                    "github": company.github_account or "",
                    "linkedin": company.linkedin_account or "",
                    "youtube": company.youtube_account or "",
                    "instagram": company.instagram_account or "",
                    "tiktok": company.tiktok_account or "",
                    "zalo": company.zalo_account or "",
                },
                "social_icons": {
                    "twitter": f"data:image/png;base64,{company.twitter_icon.decode()}" if company.twitter_icon else "",
                    "facebook": f"data:image/png;base64,{company.facebook_icon.decode()}" if company.facebook_icon else "",
                    "github": f"data:image/png;base64,{company.github_icon.decode()}" if company.github_icon else "",
                    "linkedin": f"data:image/png;base64,{company.linkedin_icon.decode()}" if company.linkedin_icon else "",
                    "youtube": f"data:image/png;base64,{company.youtube_icon.decode()}" if company.youtube_icon else "",
                    "instagram": f"data:image/png;base64,{company.instagram_icon.decode()}" if company.instagram_icon else "",
                    "tiktok": f"data:image/png;base64,{company.tiktok_icon.decode()}" if company.tiktok_icon else "",
                    "zalo": f"data:image/png;base64,{company.zalo_icon.decode()}" if company.zalo_icon else "",
                },
            }
            data.append(company_data)

        return Response(json.dumps(data), content_type='application/json', status=200)
