frappe.ui.form.on('Item Category', {
    category: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'is_new', 1);
    }
});