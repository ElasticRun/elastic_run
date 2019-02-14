# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technology and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Slab(Document):
	pass

@frappe.whitelist()
def get_items(slab):
	return frappe.get_all('Item Slab', fields = ['distinct parent as item_code'],
		filters={'slab': slab})