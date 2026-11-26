"""Payment records for the inventory service."""
from dataclasses import dataclass


@dataclass
class Payment:
    id: int
    name: str
    active: bool = True


def get_payments(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_payments(items):
    """Return only active items."""
    return [item for item in items if item.active]
