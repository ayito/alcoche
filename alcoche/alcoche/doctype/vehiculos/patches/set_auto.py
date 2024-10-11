import frappe

def execute():
	vehiculos = frappe.db.get_all("Vehiculos")
	for v in vehiculos:
		vehiculo = frappe.get_doc("Vehiculos", v)
		vehiculo.set_auto()
		vehiculo.save()

	try:
		frappe.db.commit()
	except Exception:
		frappe.db.rollback()
