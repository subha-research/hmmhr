# # Copyright (c) 2019, Frappe and Contributors
# # License: GNU General Public License v3. See license.txt


import frappe


def execute():
	frappe.reload_doc("hr", "doctype", "shift_assignment")
	if frappe.db.has_column("Shift Assignment", "date"):
		frappe.db.sql(
			"""update `tabShift Assignment`
            set end_date=date, start_date=date
            where date IS NOT NULL and start_date IS NULL and end_date IS NULL;"""
		)




# import frappe

# def execute():
#     try:
#         frappe.reload_doc("hmmerp", "doctype", "shift_assignment")
#     except:
#         try:
#             frappe.reload_doc("hmmhr", "doctype", "shift_assignment")
#         except:
#             pass  # Skip if neither module has the doctype
    
#     if frappe.db.has_column("Shift Assignment", "date"):
#         frappe.db.sql(
#             """update `tabShift Assignment`
#         set end_date=date, start_date=date
#         where date IS NOT NULL and start_date IS NULL and end_date IS NULL;"""
#         )