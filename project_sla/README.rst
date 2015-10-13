.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================================
Project Service Level Agreements
================================

Configure and measure Service Level Agreementes on your contracts and projects.



Configuration
=============

The basic steps to configure SLAs for a Project are:

  * Set Project's Working Calendar, at Project definitions, "Other Info" tab
  * Go to the Project's Analytic Account form; create and set SLA Definitions
  * Use the "Reapply SLAs" button on the Analytic Account form
  * See Project Issue's calculated SLAs in the new "Service Levels" tab


Usage
=====

Contract SLAs
-------------

SLAs are assigned to Contracts, on the Analytic Account form, SLA Definition
separator. This is also where new SLA Definitions are created.

One Contract can have several SLA Definitions attached, allowing for
"composite SLAs". For example, a contract could have a Response Time SLA (time
to start resolution) and a Resolution Time SLA (time to close request).


SLA Controlled Documents
------------------------

Only Project Issue documents are made SLA controllable.
However, a framework is made available to easilly build extensions to make
other documents models SLA controlled.

SLA controlled documents have attached information on the list of SLA rules
they should meet (more than one in the case for composite SLAs) and a summary
SLA status:

  * "watching" the service level (it has SLA requirements to meet)
  * under "warning" (limit dates are close, special attention is needed)
  * "failed" (one on the SLA limits has not been met)
  * "achieved" (all SLA limits have been met)

Transient states, such as "watching" and "warning", are regularly updated by
a hourly scheduled job, that reevaluates the warning and limit dates against
the current time and changes the state when find dates that have been exceeded.

To decide what SLA Definitions apply for a specific document, first a lookup
is made for a ``analytic_account_id`` field. If not found, then it will
look up for the ``project_id`` and it's corresponding ``analytic_account_id``.

Specifically, the Service Desk module introduces a Analytic Account field for
Project Issues. This makes it possible for a Service Team (a "Project") to
have a generic SLA, but at the same time allow for some Contracts to have
specific SLAs (such as the case for "premium" service conditions).


SLA Definitions and Rules
-------------------------

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/140/8.0

New SLA Definitions are created from the Analytic Account form, SLA Definition
field.

Each definition can have one or more Rules.
The particular rule to use is decided by conditions, so that you can set
different service levels based on request attributes, such as Priority or
Category.
Each rule condition is evaluated in "sequence" order, and the first onea to met
is the one to be used.
In the simplest case, a single rule with no condition is just what is needed.

Each rule sets a number of hours until the "limit date", and the number of
hours until a "warning date". The former will be used to decide if the SLA
was achieved, and the later can be used for automatic alarms or escalation
procedures.

Time will be counted from creation date, until the "Control Date" specified for
the SLA Definition.  That would usually be the "Close" (time until resolution)
or the "Open" (time until response) dates.

The working calendar set in the related Project definitions will be used (see
the "Other Info" tab). If none is defined, a builtin "all days, 8-12 13-17"
default calendar is used.

A timezone and leave calendars will also used, based on either the assigned
user (document's `user_id`) or on the current user.



Known issues / Roadmap
======================

* ...

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/
{project_repo}/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback `here <https://github.com/OCA/
{project_repo}/issues/new?body=module:%20
{module_name}%0Aversion:%20
{version}%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Daniel Reis (https://launchpad.net/~dreis-pt)
* David Vignoni, author of the icon from the KDE 3.x Nuvola icon theme

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
