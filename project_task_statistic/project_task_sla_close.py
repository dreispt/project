from openerp import models, fields, api
from datetime import datetime, timedelta


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
            if not(self.date_closed):
                vals['date_closed'] = fields.datetime.now(
                    ).strftime('%Y-%m-%d %H:%M:%S')
        else:
            vals['date_closed'] = None
        res = super(project_task_close_action, self).write(vals)
        return res
