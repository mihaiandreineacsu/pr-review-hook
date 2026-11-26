import unittest

from inventory.suppliers import Supplier, find_suppliers, list_active_suppliers


class SupplierTests(unittest.TestCase):
    def setUp(self):
        self.items = [Supplier(1, "a"), Supplier(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_suppliers(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_suppliers(self.items)), 1)
