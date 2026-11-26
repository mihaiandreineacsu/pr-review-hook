import unittest

from inventory.suppliers import Supplier, get_suppliers, list_active_suppliers


class SupplierTests(unittest.TestCase):
    def setUp(self):
        self.items = [Supplier(1, "A"), Supplier(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_suppliers(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_suppliers(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_suppliers(self.items)], [1])
