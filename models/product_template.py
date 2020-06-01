# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ['product.template', 'mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(track_visibility='onchange')
    description = fields.Text(track_visibility='onchange')
    description_purchase = fields.Text(track_visibility='onchange')
    description_sale = fields.Text(track_visibility='onchange')
    type = fields.Selection(track_visibility='onchange')
    rental = fields.Boolean(track_visibility='onchange')
    categ_id = fields.Many2one(track_visibility='onchange')

    currency_id = fields.Many2one(track_visibility='onchange')
    cost_currency_id = fields.Many2one(track_visibility='onchange')

    # price fields
    # price: total template price, context dependent (partner, pricelist, quantity)
    price = fields.Float(track_visibility='onchange')

    # list_price: catalog price, user defined
    list_price = fields.Float(track_visibility='onchange')

    lst_price = fields.Float(track_visibility='onchange')
    standard_price = fields.Float(track_visibility='onchange')

    volume = fields.Float(track_visibility='onchange')
    weight = fields.Float(track_visibility='onchange')
    weight_uom_id = fields.Many2one(track_visibility='onchange')
    weight_uom_name = fields.Char(track_visibility='onchange')
    sale_ok = fields.Boolean(track_visibility='onchange')
    purchase_ok = fields.Boolean(track_visibility='onchange')
    pricelist_id = fields.Many2one(track_visibility='onchange')

    uom_id = fields.Many2one(track_visibility='onchange')
    uom_name = fields.Char(track_visibility='onchange')
    uom_po_id = fields.Many2one(track_visibility='onchange')
    company_id = fields.Many2one(track_visibility='onchange')


    active = fields.Boolean(track_visibility='onchange')
    color = fields.Integer(track_visibility='onchange')

    # related to display product product information if is_product_variant
    barcode = fields.Char(track_visibility='onchange')
    default_code = fields.Char(track_visibility='onchange')
