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
    'name': 'SLA Control on Project Issues and Tasks',
    'summary': 'Install service level control for Issies and Tasks',
    'version': '1.1',
    "category": "Project Management",
    'description': """\
SLAs are defined in the Project's related Analytic Account.
See the Service Level Agreements base module for more details.

The SLA features have been split into several smaller modules.
This module makes easier to keep compatibility with existing installations.
""",
    'author': 'Daniel Reis',
    'website': '',
    'depends': [
        'project_sla_task',
        'project_sla_issue',
    ],
    'installable': True,
}
