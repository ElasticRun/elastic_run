frappe.ui.form.on('Promotional Scheme', {
    slab: function(frm) {
        if (frm.doc.slab) {
            frappe.call({
                method: "elastic_run.elastic_run.doctype.slab.slab.get_items",
                args: {
                    'slab': frm.doc.slab
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