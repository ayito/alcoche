// Copyright (c) 2024, ESB and contributors
// For license information, please see license.txt

frappe.ui.form.on("Reserva de alquiler", {
	refresh(frm) {

	},

	tasa(frm) {
		// recalcular el total
		frm.trigger("actualiza_cantidad_total");
	},

	actualiza_cantidad_total(frm) {
	let total_d = 0;
		for(let trayecto of frm.doc.trayectos) {
		    // console.log(trayecto.distancia);
			total_d += trayecto.distancia;
		}
		const cantidad_total = frm.doc.tasa * total_d;
		frm.set_value("cantidad_total", cantidad_total);
	},

});

frappe.ui.form.on('Elemento de reserva de alquiler', {
	refresh(frm) {
		// your code here
	},
	distancia(frm, cdt, cdn) {
		// ejemplos
		// console.log(cdt, cdn);
		// console.log("la distancia a cambiado en la tabla");
		// console.log(frappe.get_doc(cdt, cdn));
		// ctrayecto = frappe.get_doc(cdt, cdn);
		// cfrappe.model.set_value(cdt, cdn, "origen", "Origen actualizado");
		frm.trigger("actualiza_cantidad_total");
	},
	trayectos_remove(frm) {
		frm.trigger("actualiza_cantidad_total");
	}
})
