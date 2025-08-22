# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


# import frappe
import hmmerp
from frappe.model.document import Document


class IncomeTaxSlab(Document):
	def validate(self):
		if self.company:
			self.currency = hmmerp.get_company_currency(self.company)
