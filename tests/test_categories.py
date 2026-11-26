import unittest

from inventory.categories import Category, get_categories, list_active_categories


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.items = [Category(1, "A"), Category(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_categories(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_categories(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_categories(self.items)], [1])
