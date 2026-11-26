"""OrderItem records for the inventory service."""
from dataclasses import dataclass


@dataclass
class OrderItem:
    id: int
    name: str
    active: bool = True


def get_order_items(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_order_items(items):
    """Return only active items."""
    return [item for item in items if item.active]
