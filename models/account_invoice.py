# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class AccountPaymentTerm(models.Model):
    _inherit = ['account.payment.term', 'mail.thread', 'mail.activity.mixin']

