import unittest

from inventory.shipments import Shipment, get_shipments, list_active_shipments


class ShipmentTests(unittest.TestCase):
    def setUp(self):
        self.items = [Shipment(1, "A"), Shipment(2, "B", active=False)]

    def test_get_existing(self):
        self.assertEqual(get_shipments(self.items, 1).name, "A")

    def test_get_missing(self):
        self.assertIsNone(get_shipments(self.items, 99))

    def test_list_active(self):
        self.assertEqual([i.id for i in list_active_shipments(self.items)], [1])
