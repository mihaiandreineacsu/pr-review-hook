import unittest

from inventory.stock import Stock, get_stock, is_low_stock, list_active_stock


class StockTests(unittest.TestCase):
    def setUp(self):
        self.items = [Stock(1, "A"), Stock(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_stock(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_stock(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_stock(self.items)], [1])


class LowStockTests(unittest.TestCase):
    def test_below_threshold(self):
        self.assertTrue(is_low_stock(2))

    def test_at_threshold(self):
        self.assertTrue(is_low_stock(5))

    def test_above_threshold(self):
        self.assertFalse(is_low_stock(6))

    def test_custom_threshold(self):
        self.assertTrue(is_low_stock(10, threshold=10))

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            is_low_stock(-1)
