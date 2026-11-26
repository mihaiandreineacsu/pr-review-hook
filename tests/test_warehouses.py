import unittest

from inventory.warehouses import Warehouse, get_warehouses, list_active_warehouses


class WarehouseTests(unittest.TestCase):
    def setUp(self):
        self.items = [Warehouse(1, "A"), Warehouse(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_warehouses(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_warehouses(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_warehouses(self.items)], [1])
