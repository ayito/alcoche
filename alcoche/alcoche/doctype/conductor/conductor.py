# Copyright (c) 2024, ESB and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Conductor(Document):
	def send_alert(self):
		print("esto es una alerta!!")

