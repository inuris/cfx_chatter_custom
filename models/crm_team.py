# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Team(models.Model):
    _name = 'crm.team'
    _inherit = ['crm.team', 'mail.thread', 'mail.activity.mixin']

    use_leads = fields.Boolean(track_visibility='onchange')
    use_opportunities = fields.Boolean(track_visibility='onchange')
    alias_id = fields.Many2one(track_visibility='onchange')
    unassigned_leads_count = fields.Integer(track_visibility='onchange')
    opportunities_count = fields.Integer(track_visibility='onchange')
    opportunities_amount = fields.Integer(track_visibility='onchange')
    dashboard_graph_model = fields.Selection(track_visibility='onchange')
    dashboard_graph_period_pipeline = fields.Selection(track_visibility='onchange')
    dashboard_graph_group_pipeline = fields.Selection(track_visibility='onchange')