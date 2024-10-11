# Copyright (c) 2024, ESB and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Reservadealquiler(Document):
	def validate(self):
		if not self.tasa:
			# frappe.throw("Por favor facilita una tasa")
		    self.tasa = frappe.db.get_single_value('Configuracion Alcoche', 'tasa_estandar');

		total_distancia = 0
		for trayecto in self.trayectos:
			total_distancia += trayecto.distancia

		self.cantidad_total = total_distancia * self.tasa
