# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Daniel Reis
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
{
    'name': 'Service Level Agreements',
    'summary': 'Define SLAs for your Contracts',
    'version': '8.0.1.0.0',
    "category": "Project Management",
    'author': "Daniel Reis,Odoo Community Association (OCA)",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'project_issue',
    ],
    'data': [
        'project_sla_view.xml',
        'project_sla_control_view.xml',
        'project_sla_control_data.xml',
        'analytic_account_view.xml',
        'project_view.xml',
        'project_issue_view.xml',
        'project_task_view.xml',
        'security/ir.model.access.csv',
        'report/report_sla_view.xml',
    ],
    'demo': ['project_sla_demo.xml'],
    'test': ['test/project_sla.yml'],
    'installable': True,
}
