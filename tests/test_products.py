import unittest

from inventory.products import Product, get_products, list_active_products


class ProductTests(unittest.TestCase):
    def setUp(self):
        self.items = [Product(1, "A"), Product(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_products(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_products(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_products(self.items)], [1])
