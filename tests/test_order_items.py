import unittest

from inventory.order_items import OrderItem, find_order_items, list_active_order_items


class OrderItemTests(unittest.TestCase):
    def setUp(self):
        self.items = [OrderItem(1, "a"), OrderItem(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_order_items(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_order_items(self.items)), 1)
