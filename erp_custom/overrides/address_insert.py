import frappe
from frappe import _
@frappe.whitelist()
def upload_supplier_address(self,method=None):
    if self.supplier_name and not frappe.db.get_value("Address", {"address_title" : self.name}):
            frappe.get_doc(
                {   
                    "doctype"           : "Address",
                    "address_title"     : self.get("supplier_name"),
                    "address_type"      : self.get("erpcust_address_type"),
                    "address_line1"     : self.get("erpcust_address_line1"),
                    "city"              : self.get("erpcust_city"),
                    "state"             : self.get("erpcust_state"),
                    "country"           : self.get("country"),
                    "pincode"           : self.get("erpcust_pincode"),
                    "phone"             : self.get("erpcust_phone"),
                    "email_id"          : self.get("email_id"),
                    "gstin"             : self.get("gstin"),
                    "gst_category"      : self.get("gst_category"),
                    "is_primary_address": "1",
                    # "gst_state"       : doc.get("gst_state"),
                    # "gst_state_number": doc.get("gst_state_number"),
                    "links" : [{"link_doctype" : self.get("doctype"), "link_name" : self.get("name")}],
                },
            ).save(ignore_permissions=True)

@frappe.whitelist()
def upload_customer_address(self,method=None):
    if self.customer_name and not frappe.db.get_value("Address", {"address_title" : self.name}):
            frappe.get_doc(
                {   
                    "doctype"           : "Address",
                    "address_title"     : self.get("customer_name"),
                    "address_type"      : self.get("erpcust_address_type"),
                    "address_line1"     : self.get("erpcust_address_line1"),
                    "city"              : self.get("erpcust_city"),
                    "state"             : self.get("erpcust_state"),
                    "country"           : self.get("erpcust_country"),
                    "pincode"           : self.get("erpcust_pincode"),
                    "phone"             : self.get("erpcust_phone"),
                    "email_id"          : self.get("email_id"),
                    "gstin"             : self.get("gstin"),
                    "gst_category"      : self.get("gst_category"),
                    "is_primary_address": "1",
                    # "gst_state"       : doc.get("gst_state"),
                    # "gst_state_number": doc.get("gst_state_number"),
                    "links" : [{"link_doctype" : self.get("doctype"), "link_name" : self.get("name")}],
                },
            ).save(ignore_permissions=True)