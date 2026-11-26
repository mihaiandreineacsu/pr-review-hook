import unittest

from inventory.discounts import Discount, find_discounts, list_active_discounts


class DiscountTests(unittest.TestCase):
    def setUp(self):
        self.items = [Discount(1, "a"), Discount(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_discounts(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_discounts(self.items)), 1)
