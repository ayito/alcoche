// Copyright (c) 2024, ESB and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehiculos", {
	refresh(frm) {

	},

	obtener_el_sumario(frm) {
		frm.get_field("sumario").$wrapper.append("<h1>Hola, aquí tu sumario!<h1>")
	}
});
