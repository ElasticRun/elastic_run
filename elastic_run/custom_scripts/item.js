frappe.ui.form.on('Item Slab', {
    slab: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'is_new', 1);
    }
});