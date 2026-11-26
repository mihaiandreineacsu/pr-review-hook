import unittest

from inventory.warehouses import Warehouse, find_warehouses, list_active_warehouses


class WarehouseTests(unittest.TestCase):
    def setUp(self):
        self.items = [Warehouse(1, "a"), Warehouse(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_warehouses(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_warehouses(self.items)), 1)
