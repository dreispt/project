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

from openerp import models, fields


class Task(models.Model):
    _inherit = 'project.task'

    day_close = fields.Float('Day Close')
    day_open = fields.Float('Day Open')
    working_hours_close = fields.Float('Working Hours Close')
    working_hours_open = fields.Float('Working Hours Open')
