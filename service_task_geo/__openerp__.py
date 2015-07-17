# -*- coding: utf-8 -*-
##############################################################################
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
{'name': 'Geospatial support for project tasks',
 'version': '0.1',
 'category': 'GeoBI',
 'author': "Daniel Reis,Odoo Community Association (OCA)",
 'license': 'AGPL-3',
 'website': 'http://github.com/OCA/geospatial',
 'depends': [
     'geoengine_partner',
     'service_desk',  # from OCA/project-service
 ],
 'data': [
     'project_task_view.xml'
 ],
 'installable': True,
 }
