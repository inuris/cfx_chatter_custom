# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = ['product.category', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    complete_name = fields.Char(track_visibility='onchange')
    parent_id = fields.Many2one(track_visibility='onchange')  
