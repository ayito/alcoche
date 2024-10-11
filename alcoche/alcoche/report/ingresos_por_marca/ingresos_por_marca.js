// Copyright (c) 2024, ESB and contributors
// For license information, please see license.txt

frappe.query_reports["Ingresos por marca"] = {
	"filters" : [
		{
			"fieldname": "my_filter",
			"label": __("Seleccionar vehículo"),
			"fieldtype": "Link",
			"options": "Vehiculos",
			"reqd": 0,
		},
	],
};
