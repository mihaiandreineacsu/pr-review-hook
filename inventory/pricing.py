"""Pricing records for the inventory service."""
from dataclasses import dataclass


@dataclass
class Pricing:
    id: int
    name: str
    active: bool = True


def get_pricing(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_pricing(items):
    """Return only active items."""
    return [item for item in items if item.active]
