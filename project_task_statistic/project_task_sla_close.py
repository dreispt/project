# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Daniel Reis
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class project_task_close_action(models.Model):
    _inherit = "project.task"

    date_opened = fields.Datetime('Date Opened')
    date_closed = fields.Datetime('Date Closed')

    @api.model
    def create(self, vals):
        if not (self.date_opened) and self.stage_id.state == 'open':
            vals['date_opened'] = fields.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')

        elif self.stage_id.state in ('cancelled', 'done'):
            vals['date_closed'] = fields.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')
        else:
            vals['date_closed'] = None
        res = super(project_task_close_action, self).create(vals)
        return res

    @api.one
    def write(self, vals):
        if not (self.date_opened) and self.stage_id.state == 'open':
            vals['date_opened'] = fields.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')

        elif self.stage_id.state in ('cancelled', 'done'):
            if not self.date_closed:
                vals['date_closed'] = fields.datetime.now(
                    ).strftime('%Y-%m-%d %H:%M:%S')
                if not self.date_opened:
                    vals['date_opened'] = vals['date_closed']
        else:
            vals['date_closed'] = None
        res = super(project_task_close_action, self).write(vals)
        return res
