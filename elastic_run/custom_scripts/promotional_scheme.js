frappe.ui.form.on('Promotional Scheme', {
    category: function(frm) {
        if (frm.doc.category) {
            frappe.call({
                method: "elastic_run.elastic_run.doctype.category.category.get_items",
                args: {
                    'category': frm.doc.category
                },
                callback: function(r) {
                    if(r && r.message) {
                        frm.doc.items = [];
                        r.message.forEach(d => {
                            var row = frappe.model.add_child(frm.doc, "Apply Rule On Item Code", "items");
						    row.item_code = d.item_code;
                        })

                        refresh_field("items");
                    }
                }
            });
        }
    }
});