# Copyright (c) 2024, ESB and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestVehiculos(FrappeTestCase):
	def test_auto_configurado(self):
		test_vehiculo = frappe.new_doc("Vehiculos")
		test_vehiculo.fabricante = "Ford"
		test_vehiculo.modelo = "Focus"
		# test_vehiculo.anyo = "2007"
		test_vehiculo.color = "Green"
		test_vehiculo.caducidad_del_seguro = "2025-10-21"
		test_vehiculo.save()

		self.assertEqual(test_vehiculo.auto, "Ford Focus")
