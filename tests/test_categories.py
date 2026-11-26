import unittest

from inventory.categories import Category, find_categories, list_active_categories


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.items = [Category(1, "a"), Category(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_categories(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_categories(self.items)), 1)
