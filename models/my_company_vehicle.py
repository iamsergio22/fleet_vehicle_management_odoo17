from odoo import models, fields
from datetime import datetime, timedelta
from odoo import api
from odoo.exceptions import ValidationError

class MyCompanyVehicle(models.Model):
    _name = 'my.company.vehicle'
    _description = 'Company Vehicle'

    
    name = fields.Char(string="Name", required=True)
    license_plate = fields.Char(string="License Plate", required=True)
    fuel_type = fields.Selection(
        [('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('electric', 'Electric')],
        string="Fuel Type"
    )
    mileage = fields.Float(string="Mileage")
    last_service_date = fields.Date(string="Last Service Date")
    needs_service = fields.Boolean(
        string="Needs Service", compute='_compute_needs_service', store=True
    )
    partner_id = fields.Many2one(
    'res.partner', string="Owner", ondelete='cascade'
    )


    @api.depends('mileage', 'last_service_date')
    def _compute_needs_service(self):
        for record in self:
            six_months_ago = datetime.now().date() - timedelta(days=180)
            record.needs_service = (
                record.mileage > 20000 or
                (record.last_service_date and record.last_service_date < six_months_ago)
            )

    @api.onchange('fuel_type')
    def _onchange_fuel_type(self):
        if self.fuel_type == 'electric':
            self.mileage = 0
            
    @api.model
    def create(self, vals):
        if 'license_plate' in vals:
            existing_vehicle = self.search([('license_plate', '=', vals['license_plate'])], limit=1)
            if existing_vehicle:
                raise ValidationError("A vehicle with this license plate already exists.")
        return super(MyCompanyVehicle, self).create(vals)
    
    def schedule_service(self):
        pass