import unittest

from inventory.orders import Order, find_orders, list_active_orders


class OrderTests(unittest.TestCase):
    def setUp(self):
        self.items = [Order(1, "a"), Order(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_orders(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_orders(self.items)), 1)
