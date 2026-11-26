import unittest

from inventory.pricing import Pricing, get_pricing, list_active_pricing


class PricingTests(unittest.TestCase):
    def setUp(self):
        self.items = [Pricing(1, "A"), Pricing(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_pricing(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_pricing(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_pricing(self.items)], [1])
