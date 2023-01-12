import frappe
from frappe import _
@frappe.whitelist()
def upload_supplier_bank(self,method=None):
    if self.bank_account_no and self.account_name and not frappe.db.get_value(
        "Bank Account", {"party": self.name, "bank_account_no": self.bank_account_no}):
        frappe.get_doc(dict(
            doctype = "Bank Account",
            account_name = self.account_name,
            is_default = 1,
            branch_code = self.branch_code,
            bank = self.bank_name,
            bank_account_no = self.bank_account_no,
            party_type = "Supplier",
            party = self.name
        )).save(ignore_permissions=True)

@frappe.whitelist()
def upload_customer_bank(self,method=None):
    if self.bank_account_no and self.account_name and not frappe.db.get_value(
        "Bank Account", {"party": self.name, "bank_account_no": self.bank_account_no}):
        frappe.get_doc(dict(
            doctype = "Bank Account",
            account_name = self.account_name,
            is_default = 1,
            branch_code = self.branch_code,
            bank = self.bank_name,
            bank_account_no = self.bank_account_no,
            party_type = "Customer",
            party = self.name
        )).save(ignore_permissions=True)