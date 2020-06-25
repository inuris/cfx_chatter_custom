# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class UoMCategory(models.Model):
    _name = 'uom.category'
    _inherit = ['uom.category', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    measure_type = fields.Selection(track_visibility='onchange')

class UoM(models.Model):
    _name = 'uom.uom'
    _inherit = ['uom.uom', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    
    factor = fields.Float(track_visibility='onchange')
    factor_inv = fields.Float(track_visibility='onchange')
    rounding = fields.Float(track_visibility='onchange')
    active = fields.Boolean(track_visibility='onchange')
    uom_type = fields.Selection(track_visibility='onchange')
    measure_type = fields.Selection(track_visibility='onchange')
