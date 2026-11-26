import unittest

from inventory.order_items import OrderItem, get_order_items, list_active_order_items


class OrderItemTests(unittest.TestCase):
    def setUp(self):
        self.items = [OrderItem(1, "A"), OrderItem(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_order_items(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_order_items(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_order_items(self.items)], [1])
