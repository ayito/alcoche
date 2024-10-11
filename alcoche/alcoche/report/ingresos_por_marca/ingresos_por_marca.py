# Copyright (c) 2024, ESB and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	print("---"*20)
	frappe.errprint(filters)

	columns = get_columns()
	data = get_data()

	chart = {
		"data": {
			"labels": [x.fabricante for x in data],
			"datasets": [
				{
					"values": [x.ingresos_totales for x in data]
				}
			],
		},
		"type": "donut",
	}

	return columns, data, "Informe de ingresos por fabricante", chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Fabricante"),
			"fieldname": "fabricante",
			"fieldtype": "Data",
		},
		{
			"label": _("Ingresos Totales"),
			"fieldname": "ingresos_totales",
			"fieldtype": "Currency",
			"options": "EUR",
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	result = frappe.get_all(
		"Reserva de alquiler",
		fields=["SUM(cantidad_total) AS ingresos_totales","vehiculo.fabricante"],
		filters={"docstatus": ("<", 2)},
		group_by="fabricante",
	)

	return result
