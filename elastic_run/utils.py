# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def update_items_based_on_slab(doc, method):
    for d in doc.slabs:
        if not d.is_new:
            d.is_new = 0
            continue

        for scheme in frappe.get_all('Promotional Scheme',
            {'slab': d.slab}):
            ps_doc = frappe.get_doc('Promotional Scheme', scheme.name)

            if doc.name not in [row.item_code for row in ps_doc.items]:
                ps_doc.append('items', {
                    'item_code': doc.name
                })
                ps_doc.save()