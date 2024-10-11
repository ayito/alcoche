// Copyright (c) 2024, ESB and contributors
// For license information, please see license.txt

frappe.ui.form.on("Pedido de alquiler", {
	onload(frm) {
		console.log("cargando ...");
	},
	setup(frm) {
		console.log("configurando ...");
	},
	refresh(frm) {
		console.log("refrescando ...");
	},
	estado(frm) {
		console.log("El estado ha cambiado!!");

		if (frm.doc.estado === "Nuevo") {
			frm.add_custom_button("Aceptar", () => {
				// frappe.show_alert("botón pulsado!!!")
				frm.set_value("estado", "Aceptado");
				frm.save();
			}, "Acciones");

			frm.add_custom_button("Rechazar", () => {
				// frappe.show_alert("botón pulsado!!!")
				frm.set_value("estado", "Rechazado");
				frm.save();
			}, "Acciones");
		}
	}
});
