# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technology and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Category(Document):
	pass

@frappe.whitelist()
def get_items(category):
	return frappe.get_all('Item Category', fields = ['distinct parent as item_code'],
		filters={'category': category})