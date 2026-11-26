import unittest

from inventory.stock import Stock, find_stock, list_active_stock


class StockTests(unittest.TestCase):
    def setUp(self):
        self.items = [Stock(1, "a"), Stock(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_stock(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_stock(self.items)), 1)
