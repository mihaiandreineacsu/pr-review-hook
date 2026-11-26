import unittest

from inventory.pricing import Pricing, find_pricing, list_active_pricing


class PricingTests(unittest.TestCase):
    def setUp(self):
        self.items = [Pricing(1, "a"), Pricing(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_pricing(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_pricing(self.items)), 1)
