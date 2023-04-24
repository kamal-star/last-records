# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "last_records"
app_title = "Last Records"
app_publisher = "Hardik Gadesha"
app_description = "App to show last records of purchase and sales"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/last_records/css/last_records.css"
# app_include_js = "/assets/last_records/js/last_records.js"

# include js, css files in header of web template
# web_include_css = "/assets/last_records/css/last_records.css"
# web_include_js = "/assets/last_records/js/last_records.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

	# "Purchase Order" : "public/js/purchase_order.js"
doctype_js = {
	"Purchase Invoice" : "public/js/purchase_invoice.js",
    "Sales Invoice" : "public/js/sales_invoice.js"}


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
# get_website_user_home_page = "last_records.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "last_records.install.before_install"
# after_install = "last_records.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "last_records.notifications.get_notification_config"

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

fixtures = [
	{
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
			"Purchase Order-section_break_56",
			"Purchase Order-last_purchase_details",
			"Sales Order-last_sales_details",
			"Sales Order-last_sales_table"
		]
	   ]
	]
	},
	{
        "doctype": "Role",
        "filters": [
            [
                "name",
                "in",
                [
                        "Stock Popup"
                ]
           ]
        ]
    }
]

# doc_events = {
#     "Sales Invoice": {
#         "after_insert":"last_records.custom_methods.create_si_from_sr"
# 		#"on_submit": "bulk_document_creation.bulk_document_creation.doctype.bulk_invoice_creation.bulk_invoice_creation.upd_b2c"
#         },
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"last_records.tasks.all"
# 	],
# 	"daily": [
# 		"last_records.tasks.daily"
# 	],
# 	"hourly": [
# 		"last_records.tasks.hourly"
# 	],
# 	"weekly": [
# 		"last_records.tasks.weekly"
# 	]
# 	"monthly": [
# 		"last_records.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "last_records.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "last_records.event.get_events"
# }

