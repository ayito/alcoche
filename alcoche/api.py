import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
	return "😊"

def throw_emoji(doc, event):
	frappe.throw("😊")

def enviar_recuerdos():
	pass

def get_permission_query_conditions(user):
	# frappe.throw(user)
	return f'name IN (1, 2, 3)'
