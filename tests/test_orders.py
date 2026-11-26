import unittest

from inventory.orders import Order, get_orders, list_active_orders


class OrderTests(unittest.TestCase):
    def setUp(self):
        self.items = [Order(1, "A"), Order(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_orders(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_orders(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_orders(self.items)], [1])
