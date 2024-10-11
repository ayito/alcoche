# Copyright (c) 2024, ESB and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehiculos(WebsiteGenerator):
	def before_save(self):
		self.set_auto()

	def set_auto(self):
		self.auto = f"{self.fabricante} {self.modelo}, {self.anyo}"



