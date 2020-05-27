# -*- coding: utf-8 -*-
import logging

from datetime import datetime, time
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.addons.resource.models.resource import HOURS_PER_DAY
from odoo.exceptions import AccessError, UserError
from odoo.tools.translate import _
from odoo.tools.float_utils import float_round

_logger = logging.getLogger(__name__)

class HolidaysAllocation(models.Model):
    """ Allocation Requests Access specifications: similar to leave requests """ 
    _inherit = "hr.leave.allocation"

    @api.model
    def _update_accrual(self):
        """
            Method called by the cron task in order to increment the number_of_days when
            necessary.
        """
        today = fields.Date.from_string(fields.Date.today())

        holidays = self.search([('accrual', '=', True), ('employee_id.active', '=', True), ('state', '=', 'validate'), ('holiday_type', '=', 'employee'),
                                '|', ('date_to', '=', False), ('date_to', '>', fields.Datetime.now()),
                                '|', ('nextcall', '=', False), ('nextcall', '<=', today)])


        for holiday in holidays:
            values = {}

            delta = relativedelta(days=0)

            if holiday.interval_unit == 'weeks':
                delta = relativedelta(weeks=holiday.interval_number)
            if holiday.interval_unit == 'months':
                delta = relativedelta(months=holiday.interval_number)
            if holiday.interval_unit == 'years':
                delta = relativedelta(years=holiday.interval_number)

            if holiday.nextcall:
                values['nextcall'] = holiday.nextcall + delta
                days_to_give = holiday.number_per_interval
                if holiday.unit_per_interval == 'hours':
                    # As we encode everything in days in the database we need to convert
                    # the number of hours into days for this we use the
                    # mean number of hours set on the employee's calendar
                    days_to_give = days_to_give / HOURS_PER_DAY

                values['number_of_days'] = holiday.number_of_days + days_to_give
                if holiday.accrual_limit > 0:
                    values['number_of_days'] = min(values['number_of_days'], holiday.accrual_limit)
            else:
                values['nextcall'] = today.replace(day=1) + delta
            
            holiday.write(values)

