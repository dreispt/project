# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Daniel Reis
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


class ServiceItem(models.Model):
    _name = 'service.item'
    _description = "Service Item"

    name = fields.Char('Name')
    code = fields.Char('Code')
    site_id = fields.Many2one(string='Site', comodel_name='res.partner')
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('active', 'Active'),
                   ('close', 'Closed')])
    date_installation = fields.Date('Installation Date')

    analytic_account_id = fields.Many2one(
        string='Contract',
        comodel_name='account.analytic.account')
    department_id = fields.Many2one(
        string='Department',
        related='analytic_account_id.department_id')
    partner_id = fields.Many2one(
        string='Customer',
        related='analytic_account_id.partner_id')

    item_group_id = fields.Many2one(
        string="Item Group",
        comodel_name='service.item.group')
    contract_group_id = fields.Many2one(
        string="Contract Group",
        comodel_name='service.contract.group')


class ServiceItemGroup(models.Model):
    _name = 'service.item.group'
    _description = "Service Item Group"

    name = fields.Char('Name')
    description = fields.Char('Description')


class ServiceContractGroup(models.Model):
    _name = 'service.contract.group'
    _description = "Service Contract Group"

    name = fields.Char('Name')
    description = fields.Char('Description')
