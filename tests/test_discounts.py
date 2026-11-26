import unittest

from inventory.discounts import Discount, get_discounts, list_active_discounts


class DiscountTests(unittest.TestCase):
    def setUp(self):
        self.items = [Discount(1, "A"), Discount(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_discounts(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_discounts(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_discounts(self.items)], [1])
