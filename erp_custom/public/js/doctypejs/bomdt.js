frappe.ui.form.on('BOM', {
    refresh(frm) {
        frm.trigger("onload")
    },
    onload(frm) {
    frm.set_query("item", function () {
        return {
            "filters": {
                "item_group": "Products"
            }
        };
    })
},
})