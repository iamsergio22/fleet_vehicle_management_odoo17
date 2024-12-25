from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vehicle_ids = fields.One2many(
        'my.company.vehicle', 'partner_id', string="Vehicles"
    )    

    vehicle_count = fields.Integer(
        string="Vehicle Count", compute='_compute_vehicle_count'
    )


    @api.depends('vehicle_ids')
    def _compute_vehicle_count(self):
        for partner in self:
            partner.vehicle_count = len(partner.vehicle_ids)
