from . import __version__ as app_version

app_name = "erp_custom"
app_title = "ERP Custom"
app_publisher = "Prashant Kamble"
app_description = "This app All Default site Customization incorporate for easy to use."
app_email = "kambleprashant@outlook.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp_custom/css/erp_custom.css"
# app_include_js = "/assets/erp_custom/js/erp_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp_custom/css/erp_custom.css"
# web_include_js = "/assets/erp_custom/js/erp_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erp_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Supplier" : "public/js/doctypejs/addressimport.js"    }
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "erp_custom.utils.jinja_methods",
#	"filters": "erp_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erp_custom.install.before_install"
# after_install = "erp_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erp_custom.uninstall.before_uninstall"
# after_uninstall = "erp_custom.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# ~~~~~~~~~~~~~~~~ BOM Doctype Client Script Hook ~~~~~~~~~~~~~~~~~~~~~~
doctype_js = {
	"BOM":"public/js/doctypejs/bomdt.js" # BOM Item Filter Based on Finish Good Hook
}

doc_events = {

    # ~~~~~~~~~~~~~~~~ Supplier/Customer Import Hook ~~~~~~~~~~~~~~~~~~~~~~
	"Supplier": {
		"after_insert": [
            "erp_custom.overrides.bank_insert.upload_supplier_bank",        # ~~~~~~ Upload Bank Details
            "erp_custom.overrides.address_insert.upload_supplier_address"   # ~~~~~~ Upload Address
        ]},
    "Customer":{
        "after_insert": [
            "erp_custom.overrides.bank_insert.upload_customer_bank",        # ~~~~~~ Upload Bank Details
            "erp_custom.overrides.address_insert.upload_customer_address"   # ~~~~~~ Upload Address
        ]}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erp_custom.tasks.all"
#	],
#	"daily": [
#		"erp_custom.tasks.daily"
#	],
#	"hourly": [
#		"erp_custom.tasks.hourly"
#	],
#	"weekly": [
#		"erp_custom.tasks.weekly"
#	],
#	"monthly": [
#		"erp_custom.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "erp_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erp_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erp_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erp_custom.auth.validate"
# ]
fixtures = [{"dt": "Custom Field", "filters": [
        [
            "name", "in", 
            [
                "Item-old_erp_item_code",

                "Supplier-erp_custom",
                "Supplier-address_details",
                "Supplier-erpcust_address_type",
                "Supplier-erpcust_address_line1",
                "Supplier-erpcust_city",
                "Supplier-cb",
                "Supplier-erpcust_state",
                "Supplier-erpcust_pincode",
                "Supplier-erpcust_phone",
                "Supplier-bank_details",
                "Supplier-account_name",
                "Supplier-bank_name",
                "Supplier-cb2",
                "Supplier-branch_code",
                "Supplier-bank_account_no",
                
                "Customer-erp_custom",
                "Customer-address_details",
                "Customer-erpcust_address_type",
                "Customer-erpcust_address_line1",
                "Customer-erpcust_city",
                "Customer-cb",
                "Customer-erpcust_state",
                "Customer-erpcust_pincode",
                "Customer-erpcust_country",
                "Customer-erpcust_phone",
                "Customer-bank_details",
                "Customer-account_name",
                "Customer-bank_name",
                "Customer-cb2",
                "Customer-branch_code",
                "Customer-bank_account_no",
            ]
        ]
    ]},
]