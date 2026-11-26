"""Stock records for the inventory service."""
from dataclasses import dataclass


@dataclass
class Stock:
    id: int
    name: str
    active: bool = True


def get_stock(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_stock(items):
    """Return only active items."""
    return [item for item in items if item.active]


LOW_STOCK_THRESHOLD = 5


def is_low_stock(quantity, threshold=LOW_STOCK_THRESHOLD):
    """Return True when the quantity is at or below the threshold.

    Negative quantities are invalid and raise ValueError.
    """
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return quantity <= threshold
