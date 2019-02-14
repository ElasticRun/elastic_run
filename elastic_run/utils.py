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
            doc = frappe.get_doc('Promotional Scheme', scheme.name)
            doc.append('items', {
                'item_code': doc.name
            })
            doc.save()