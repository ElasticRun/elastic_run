# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "elastic_run"
app_title = "Elastic Run"
app_publisher = "Frappe Technology"
app_description = "Tags Feature"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rohit@erpnext.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/elastic_run/css/elastic_run.css"
# app_include_js = "/assets/elastic_run/js/elastic_run.js"

# include js, css files in header of web template
# web_include_css = "/assets/elastic_run/css/elastic_run.css"
# web_include_js = "/assets/elastic_run/js/elastic_run.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "elastic_run.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "elastic_run.install.before_install"
# after_install = "elastic_run.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "elastic_run.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Item": {
        "validate": "elastic_run.utils.update_items_based_on_slab",
    }
}

doctype_js = {
    "Item": ["custom_scripts/item.js"],
    "Promotional Scheme": ["custom_scripts/promotional_scheme.js"],
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"elastic_run.tasks.all"
# 	],
# 	"daily": [
# 		"elastic_run.tasks.daily"
# 	],
# 	"hourly": [
# 		"elastic_run.tasks.hourly"
# 	],
# 	"weekly": [
# 		"elastic_run.tasks.weekly"
# 	]
# 	"monthly": [
# 		"elastic_run.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "elastic_run.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "elastic_run.event.get_events"
# }

