import unittest

from inventory.shipments import Shipment, find_shipments, list_active_shipments


class ShipmentTests(unittest.TestCase):
    def setUp(self):
        self.items = [Shipment(1, "a"), Shipment(2, "b", active=False)]

    def test_find_existing(self):
        self.assertEqual(find_shipments(self.items, 1).name, "A")

    def test_list_active(self):
        self.assertEqual(len(list_active_shipments(self.items)), 1)
