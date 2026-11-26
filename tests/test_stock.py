import unittest

from inventory.stock import Stock, get_stock, list_active_stock


class StockTests(unittest.TestCase):
    def setUp(self):
        self.items = [Stock(1, "A"), Stock(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_stock(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_stock(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_stock(self.items)], [1])
