# app_name = "hmmhr"
# app_title = "hmmhr"
# app_publisher = "Soumen Chowdhury"
# app_description = "Hidden Markov Model"
# app_email = "soumene0008@outlook.com"
# app_license = "mit"

# # Apps
# # ------------------

# # required_apps = []

# # Each item in the list will be shown as an app in the apps page
# # add_to_apps_screen = [
# # 	{
# # 		"name": "hmmhr",
# # 		"logo": "/assets/hmmhr/logo.png",
# # 		"title": "hmmhr",
# # 		"route": "/hmmhr",
# # 		"has_permission": "hmmhr.api.permission.has_app_permission"
# # 	}
# # ]

# # Includes in <head>
# # ------------------

# # include js, css files in header of desk.html
# # app_include_css = "/assets/hmmhr/css/hmmhr.css"
# # app_include_js = "/assets/hmmhr/js/hmmhr.js"

# # include js, css files in header of web template
# # web_include_css = "/assets/hmmhr/css/hmmhr.css"
# # web_include_js = "/assets/hmmhr/js/hmmhr.js"

# # include custom scss in every website theme (without file extension ".scss")
# # website_theme_scss = "hmmhr/public/scss/website"

# # include js, css files in header of web form
# # webform_include_js = {"doctype": "public/js/doctype.js"}
# # webform_include_css = {"doctype": "public/css/doctype.css"}

# # include js in page
# # page_js = {"page" : "public/js/file.js"}

# # include js in doctype views
# # doctype_js = {"doctype" : "public/js/doctype.js"}
# # doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# # doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# # doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# # Svg Icons
# # ------------------
# # include app icons in desk
# # app_include_icons = "hmmhr/public/icons.svg"

# # Home Pages
# # ----------

# # application home page (will override Website Settings)
# # home_page = "login"

# # website user home page (by Role)
# # role_home_page = {
# # 	"Role": "home_page"
# # }

# # Generators
# # ----------

# # automatically create page for each record of this doctype
# # website_generators = ["Web Page"]

# # automatically load and sync documents of this doctype from downstream apps
# # importable_doctypes = [doctype_1]

# # Jinja
# # ----------

# # add methods and filters to jinja environment
# # jinja = {
# # 	"methods": "hmmhr.utils.jinja_methods",
# # 	"filters": "hmmhr.utils.jinja_filters"
# # }

# # Installation
# # ------------

# # before_install = "hmmhr.install.before_install"
# # after_install = "hmmhr.install.after_install"

# # Uninstallation
# # ------------

# # before_uninstall = "hmmhr.uninstall.before_uninstall"
# # after_uninstall = "hmmhr.uninstall.after_uninstall"

# # Integration Setup
# # ------------------
# # To set up dependencies/integrations with other apps
# # Name of the app being installed is passed as an argument

# # before_app_install = "hmmhr.utils.before_app_install"
# # after_app_install = "hmmhr.utils.after_app_install"

# # Integration Cleanup
# # -------------------
# # To clean up dependencies/integrations with other apps
# # Name of the app being uninstalled is passed as an argument

# # before_app_uninstall = "hmmhr.utils.before_app_uninstall"
# # after_app_uninstall = "hmmhr.utils.after_app_uninstall"

# # Desk Notifications
# # ------------------
# # See frappe.core.notifications.get_notification_config

# # notification_config = "hmmhr.notifications.get_notification_config"

# # Permissions
# # -----------
# # Permissions evaluated in scripted ways

# # permission_query_conditions = {
# # 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# # }
# #
# # has_permission = {
# # 	"Event": "frappe.desk.doctype.event.event.has_permission",
# # }

# # Document Events
# # ---------------
# # Hook on document methods and events

# # doc_events = {
# # 	"*": {
# # 		"on_update": "method",
# # 		"on_cancel": "method",
# # 		"on_trash": "method"
# # 	}
# # }

# # Scheduled Tasks
# # ---------------

# # scheduler_events = {
# # 	"all": [
# # 		"hmmhr.tasks.all"
# # 	],
# # 	"daily": [
# # 		"hmmhr.tasks.daily"
# # 	],
# # 	"hourly": [
# # 		"hmmhr.tasks.hourly"
# # 	],
# # 	"weekly": [
# # 		"hmmhr.tasks.weekly"
# # 	],
# # 	"monthly": [
# # 		"hmmhr.tasks.monthly"
# # 	],
# # }

# # Testing
# # -------

# # before_tests = "hmmhr.install.before_tests"

# # Overriding Methods
# # ------------------------------
# #
# # override_whitelisted_methods = {
# # 	"frappe.desk.doctype.event.event.get_events": "hmmhr.event.get_events"
# # }
# #
# # each overriding function accepts a `data` argument;
# # generated from the base implementation of the doctype dashboard,
# # along with any modifications made in other Frappe apps
# # override_doctype_dashboards = {
# # 	"Task": "hmmhr.task.get_dashboard_data"
# # }

# # exempt linked doctypes from being automatically cancelled
# #
# # auto_cancel_exempted_doctypes = ["Auto Repeat"]

# # Ignore links to specified DocTypes when deleting documents
# # -----------------------------------------------------------

# # ignore_links_on_delete = ["Communication", "ToDo"]

# # Request Events
# # ----------------
# # before_request = ["hmmhr.utils.before_request"]
# # after_request = ["hmmhr.utils.after_request"]

# # Job Events
# # ----------
# # before_job = ["hmmhr.utils.before_job"]
# # after_job = ["hmmhr.utils.after_job"]

# # User Data Protection
# # --------------------

# # user_data_fields = [
# # 	{
# # 		"doctype": "{doctype_1}",
# # 		"filter_by": "{filter_by}",
# # 		"redact_fields": ["{field_1}", "{field_2}"],
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_2}",
# # 		"filter_by": "{filter_by}",
# # 		"partial": 1,
# # 	},
# # 	{
# # 		"doctype": "{doctype_3}",
# # 		"strict": False,
# # 	},
# # 	{
# # 		"doctype": "{doctype_4}"
# # 	}
# # ]

# # Authentication and authorization
# # --------------------------------

# # auth_hooks = [
# # 	"hmmhr.auth.validate"
# # ]

# # Automatically update python controller files with type annotations for this app.
# # export_python_type_annotations = True

# # default_log_clearing_doctypes = {
# # 	"Logging DocType Name": 30  # days to retain logs
# # }





app_name = "hmmhr"
app_title = "HR"
app_publisher = "Soumen Chowdhury"
app_description = "Human Resource Management System"
required_apps = ["frappe/hmmerp"]
app_logo_url = "/assets/hmmhr/images/frappe-hmmhr-logo.svg"
app_email = "soumene0008@outlook.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "hmmhr",
		"logo": "/assets/hmmhr/images/frappe-hmmhr-logo.svg",
		"title": "HR",
		"route": "/app/overview",
		"has_permission": "hmmhr.hr.utils.check_app_permission",
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hmmhr/css/hmmhr.css"
app_include_js = [
	"hmmhr.bundle.js",
]
app_include_css = "hmmhr.bundle.css"

# include js, css files in header of web template
# web_include_css = "/assets/hmmhr/css/hmmhr.css"
# web_include_js = "/assets/hmmhr/js/hmmhr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hmmhr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Employee": "public/js/hmmerp/employee.js",
	"Company": "public/js/hmmerp/company.js",
	"Department": "public/js/hmmerp/department.js",
	"Timesheet": "public/js/hmmerp/timesheet.js",
	"Payment Entry": "public/js/hmmerp/payment_entry.js",
	"Journal Entry": "public/js/hmmerp/journal_entry.js",
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

calendars = ["Leave Application"]

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Job Opening"]

website_route_rules = [
	{"from_route": "/hmmhr/<path:app_path>", "to_route": "hmmhr"},
	{"from_route": "/hmmhr_hr/<path:app_path>", "to_route": "roster"},
]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
	"methods": [
		"hmmhr.utils.get_country",
	],
}

# Installation
# ------------

# before_install = "hmmhr.install.before_install"
after_install = "hmmhr.install.after_install"
after_migrate = "hmmhr.setup.update_select_perm_after_install"

setup_wizard_complete = "hmmhr.subscription_utils.update_hmmerp_access"

# Uninstallation
# ------------

before_uninstall = "hmmhr.uninstall.before_uninstall"
# after_uninstall = "hmmhr.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hmmhr.utils.before_app_install"
after_app_install = "hmmhr.setup.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

before_app_uninstall = "hmmhr.setup.before_app_uninstall"
# after_app_uninstall = "hmmhr.utils.after_app_uninstall"

# Permissions
# -----------
# Permissions evaluated in scripted ways

has_upload_permission = {"Employee": "hmmerp.setup.doctype.employee.employee.has_upload_permission"}

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Employee": "hmmhr.overrides.employee_master.EmployeeMaster",
	"Timesheet": "hmmhr.overrides.employee_timesheet.EmployeeTimesheet",
	"Payment Entry": "hmmhr.overrides.employee_payment_entry.EmployeePaymentEntry",
	"Project": "hmmhr.overrides.employee_project.EmployeeProject",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"User": {
		"validate": "hmmerp.setup.doctype.employee.employee.validate_employee_role",
	},
	"Company": {
		"validate": "hmmhr.overrides.company.validate_default_accounts",
		"on_update": [
			"hmmhr.overrides.company.make_company_fixtures",
			"hmmhr.overrides.company.set_default_hr_accounts",
		],
		"on_trash": "hmmhr.overrides.company.handle_linked_docs",
	},
	"Holiday List": {
		"on_update": "hmmhr.utils.holiday_list.invalidate_cache",
		"on_trash": "hmmhr.utils.holiday_list.invalidate_cache",
	},
	"Timesheet": {"validate": "hmmhr.hr.utils.validate_active_employee"},
	"Payment Entry": {
		"on_submit": "hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
		"on_cancel": "hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
		"on_update_after_submit": "hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
	},
	"Journal Entry": {
		"validate": "hmmhr.hr.doctype.expense_claim.expense_claim.validate_expense_claim_in_jv",
		"on_submit": [
			"hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
			"hmmhr.hr.doctype.full_and_final_statement.full_and_final_statement.update_full_and_final_statement_status",
			"hmmhr.payroll.doctype.salary_withholding.salary_withholding.update_salary_withholding_payment_status",
		],
		"on_update_after_submit": "hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
		"on_cancel": [
			"hmmhr.hr.doctype.expense_claim.expense_claim.update_payment_for_expense_claim",
			"hmmhr.payroll.doctype.salary_slip.salary_slip.unlink_ref_doc_from_salary_slip",
			"hmmhr.hr.doctype.full_and_final_statement.full_and_final_statement.update_full_and_final_statement_status",
			"hmmhr.payroll.doctype.salary_withholding.salary_withholding.update_salary_withholding_payment_status",
		],
	},
	"Loan": {"validate": "hmmhr.hr.utils.validate_loan_repay_from_salary"},
	"Employee": {
		"validate": "hmmhr.overrides.employee_master.validate_onboarding_process",
		"on_update": [
			"hmmhr.overrides.employee_master.update_approver_role",
			"hmmhr.overrides.employee_master.publish_update",
		],
		"after_insert": "hmmhr.overrides.employee_master.update_job_applicant_and_offer",
		"on_trash": "hmmhr.overrides.employee_master.update_employee_transfer",
		"after_delete": "hmmhr.overrides.employee_master.publish_update",
	},
	"Project": {"validate": "hmmhr.controllers.employee_boarding_controller.update_employee_boarding_status"},
	"Task": {"on_update": "hmmhr.controllers.employee_boarding_controller.update_task"},
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": [
		"hmmhr.hr.doctype.interview.interview.send_interview_reminder",
	],
	"hourly": [
		"hmmhr.hr.doctype.daily_work_summary_group.daily_work_summary_group.trigger_emails",
	],
	"hourly_long": [
		"hmmhr.hr.doctype.shift_type.shift_type.update_last_sync_of_checkin",
		"hmmhr.hr.doctype.shift_type.shift_type.process_auto_attendance_for_all_shifts",
		"hmmhr.hr.doctype.shift_schedule_assignment.shift_schedule_assignment.process_auto_shift_creation",
	],
	"daily": [
		"hmmhr.controllers.employee_reminders.send_birthday_reminders",
		"hmmhr.controllers.employee_reminders.send_work_anniversary_reminders",
		"hmmhr.hr.doctype.daily_work_summary_group.daily_work_summary_group.send_summary",
		"hmmhr.hr.doctype.interview.interview.send_daily_feedback_reminder",
		"hmmhr.hr.doctype.job_opening.job_opening.close_expired_job_openings",
	],
	"daily_long": [
		"hmmhr.hr.doctype.leave_ledger_entry.leave_ledger_entry.process_expired_allocation",
		"hmmhr.hr.utils.generate_leave_encashment",
		"hmmhr.hr.utils.allocate_earned_leaves",
	],
	"weekly": ["hmmhr.controllers.employee_reminders.send_reminders_in_advance_weekly"],
	"monthly": ["hmmhr.controllers.employee_reminders.send_reminders_in_advance_monthly"],
}

advance_payment_payable_doctypes = ["Leave Encashment", "Gratuity", "Employee Advance"]

invoice_doctypes = ["Expense Claim"]

period_closing_doctypes = ["Payroll Entry"]

accounting_dimension_doctypes = [
	"Expense Claim",
	"Expense Claim Detail",
	"Expense Taxes and Charges",
	"Payroll Entry",
	"Leave Encashment",
]

bank_reconciliation_doctypes = ["Expense Claim"]

# Testing
# -------

before_tests = "hmmhr.tests.test_utils.before_tests"

# Overriding Methods
# -----------------------------

# get matching queries for Bank Reconciliation
get_matching_queries = "hmmhr.hr.utils.get_matching_queries"

regional_overrides = {
	"India": {
		"hmmhr.hr.utils.calculate_annual_eligible_hra_exemption": "hmmhr.regional.india.utils.calculate_annual_eligible_hra_exemption",
		"hmmhr.hr.utils.calculate_hra_exemption_for_period": "hmmhr.regional.india.utils.calculate_hra_exemption_for_period",
		"hmmhr.hr.utils.calculate_tax_with_marginal_relief": "hmmhr.regional.india.utils.calculate_tax_with_marginal_relief",
	},
}

# ERPNext doctypes for Global Search
global_search_doctypes = {
	"Default": [
		{"doctype": "Salary Slip", "index": 19},
		{"doctype": "Leave Application", "index": 20},
		{"doctype": "Expense Claim", "index": 21},
		{"doctype": "Employee Grade", "index": 37},
		{"doctype": "Job Opening", "index": 39},
		{"doctype": "Job Applicant", "index": 40},
		{"doctype": "Job Offer", "index": 41},
		{"doctype": "Salary Structure Assignment", "index": 42},
		{"doctype": "Appraisal", "index": 43},
	],
}

override_doctype_dashboards = {
	"Employee": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_employee",
	"Holiday List": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_holiday_list",
	"Task": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_project",
	"Project": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_project",
	"Timesheet": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_timesheet",
	"Bank Account": "hmmhr.overrides.dashboard_overrides.get_dashboard_for_bank_account",
}

ignore_links_on_delete = ["PWA Notification"]

company_data_to_be_ignored = [
	"Salary Component Account",
	"Salary Structure",
	"Salary Structure Assignment",
	"Payroll Period",
	"Income Tax Slab",
	"Leave Period",
	"Leave Policy Assignment",
	"Employee Onboarding Template",
	"Employee Separation Template",
]