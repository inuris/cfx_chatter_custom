# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountPaymentTerm(models.Model):
    _name = "account.payment.term"
    _inherit = ['account.payment.term', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    active = fields.Boolean(track_visibility='onchange')
    note = fields.Text(track_visibility='onchange')
