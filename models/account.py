# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountAccount(models.Model):
    _name = "account.account"
    _inherit = ['account.account', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    code = fields.Char(track_visibility='onchange')
    user_type_id = fields.Many2one(track_visibility='onchange')
    group_id = fields.Many2one(track_visibility='onchange')
    currency_id = fields.Many2one(track_visibility='onchange')