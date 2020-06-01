# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Lead(models.Model):
    _name = "crm.lead"
    _inherit = ['crm.lead', 'mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(track_visibility='onchange')
    partner_id = fields.Many2one(track_visibility='onchange')
    active = fields.Boolean(track_visibility='onchange')
    email_from = fields.Char(track_visibility='onchange')
    website = fields.Char(track_visibility='onchange')
    team_id = fields.Many2one(track_visibility='onchange')
    kanban_state = fields.Selection(track_visibility='onchange')
    email_cc = fields.Text(track_visibility='onchange')
    description = fields.Text(track_visibility='onchange')
    contact_name = fields.Char(track_visibility='onchange')
    partner_name = fields.Char(track_visibility='onchange')
    type = fields.Selection(track_visibility='onchange')
    priority = fields.Selection(track_visibility='onchange')
    date_closed = fields.Datetime(track_visibility='onchange')

    stage_id = fields.Many2one(track_visibility='onchange')
    user_id = fields.Many2one(track_visibility='onchange')
    referred = fields.Char(track_visibility='onchange')


    day_open = fields.Float(track_visibility='onchange')
    day_close = fields.Float(track_visibility='onchange')
    date_last_stage_update = fields.Datetime(track_visibility='onchange')


    mobile = fields.Char(track_visibility='onchange')
    function = fields.Char(track_visibility='onchange')
    title = fields.Many2one(track_visibility='onchange')