import frappe
from datetime import timedelta, date



@frappe.whitelist()
def get_bom_values(bom):
    qtty= frappe.db.get_value("BOM",{"name":bom},["quantity"])
    get_items= frappe.db.get_list("BOM Item",filters={"parent":bom},fields=["name","item_code","item_name","qty","rate","amount"])
    return(get_items,qtty)


@frappe.whitelist()
def get_operation_value(bom):
    operation_value=frappe.db.get_all("BOM Operation", filters={"parent":bom}, fields=["operation",'workstation','time_in_mins','hour_rate','operating_cost','batch_size','description'])
    qtty= frappe.db.get_value("BOM",{"name":bom},["quantity"])
    if operation_value:
        return(operation_value,qtty)
    # operation_value=frappe.db.sql("""
    # select *
    # from `tabBOM Operation`
    # where `tabBOM Operation`.name = "{0}"
    # """.format(bom),as_dict=1)

@frappe.whitelist()
def get_scrap_value(bom):
    scrap_value=frappe.db.get_all("BOM Scrap Item", filters={"parent":bom}, fields=["name","item_code","item_name","stock_qty","rate","amount"])
    qtty= frappe.db.get_value("BOM",{"name":bom},["quantity"])
    if scrap_value:
        return(scrap_value,qtty)

@frappe.whitelist()
def get_exploded_value(bom):
    exploded_value=frappe.db.get_all("BOM Explosion Item", filters={"parent":bom}, fields=["item_code",'item_name','description','stock_qty','stock_uom','rate','amount','qty_consumed_per_unit'])
    qtty= frappe.db.get_value("BOM",{"name":bom},["quantity"])
    if exploded_value:
        return(exploded_value,qtty)


@frappe.whitelist()
def set_pterms(doc,method=None):
    for d in doc.payment_schedule:
        if d.payment_term:
            kr = frappe.db.get_value("Payment Term",{"name":d.payment_term}, ["due_date_based_on"])
            dys = frappe.db.get_value("Payment Term",{"name":d.payment_term}, ["credit_days"])
            if kr=="receipt":
                d.due_date=date.today() + timedelta(days=dys)
    # kr = frappe.db.get_value("Payment Term",{"name":term}, ["due_date_based_on"])
    # dys = frappe.db.get_value("Payment Term",{"name":term}, ["credit_days"])
    # if kr=='receipt':
    #     due_date=date.today() + timedelta(days=dys)
    #     return due_date


@frappe.whitelist()
def set_actual_qty(item_code,warehouse):
    qty= frappe.db.get_value("Bin",{"item_code":item_code,"warehouse":warehouse},["actual_qty"])
    return qty
    

