from odoo import http
from odoo.http import request

class WebsiteAbout(http.Controller):

    @http.route('', type='json', auth='public', website=True)
    def about_us(self):
        # Lấy ID của công ty hiện tại từ context
        allowed_company_ids = request.env.context.get('allowed_company_ids', [])
        company = request.env['res.company'].sudo().browse(allowed_company_ids[0]) if allowed_company_ids else request.env.company
        return {
            'about_us': company.about_us or "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore."
        }
