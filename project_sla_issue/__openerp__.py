# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 - 2014 Daniel Reis
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
    'name': 'SLA Control on Project Issues',
    'summary': 'Define and control service levels on Project Issues',
    'version': '1.1',
    "category": "Project Management",
    'description': """\
SLAs are defined in the Project's related Analytic Account.
See the Service Level Agreements base module for more details.
""",
    'author': 'Daniel Reis',
    'website': '',
    'depends': [
        'project_sla_base',
        'project_issue',
    ],
    'data': [
        'project_issue_view.xml',
    ],
    'demo': ['project_sla_demo.xml'],
    'test': ['test/project_sla.yml'],
    'installable': True,
}
