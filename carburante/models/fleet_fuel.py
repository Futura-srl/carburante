from odoo import fields, models


class FleetFuelType(models.Model):
    name = "fleet.fuel.type"
    description = "Type of fuel"
    
    name = fields.Char()
    
    
class FleetFuelCompany(models.Model):
    name = "fleet.fuel.company"
    description = "Tabella per associare azienda interna con codice azienda carburante"
    
    company = fields.One2Many('res.company')
    company_reference = fields.Char()


class FleetFuel(models.Model):
    name = "fleet.fuel"
    businnes_name = fields.Char()
    reference = fields.Char()
    point_sale_code = fields.Char()
    location = fields.Char()
    address = fields.Char()
    transaction_datetime = fields.Datetime()
    ticket = fields.Char()
    km_fleet = fields.Char()
    driver = fields.One2many('res.partner')
    card_number = fields.Char()
    fleet = fields.One2many()
    product = fields.One2many('fleet.fuel.type')
    quantity = fields.Float()
    price_unit = fields.Float(digits=(3, 3))
    price = fields.Float(digits=(3, 3))
    tax = fields.Float(digits=(3, 3))
    invoice = fields.Char()
    invoice_date = fields.Date()
    invoice_discount = fields.Float(digits=(3, 3))
    tax_rate = fields.Float(digits=(3, 3))
    price_whitout_tax = fields.Float(digits=(6, 3))
    
