"""Search records for the inventory service."""
from dataclasses import dataclass


@dataclass
class Search:
    id: int
    name: str
    active: bool = True


def get_search(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_search(items):
    """Return only active items."""
    return [item for item in items if item.active]
