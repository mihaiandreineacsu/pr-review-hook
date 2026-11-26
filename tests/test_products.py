import unittest

from inventory.products import Product, find_products, list_active_products


class ProductTests(unittest.TestCase):
    def setUp(self):
        self.items = [Product(1, "a"), Product(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_products(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_products(self.items)), 1)
