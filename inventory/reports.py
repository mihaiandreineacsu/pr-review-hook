"""Report records for the inventory service."""
from dataclasses import dataclass


@dataclass
class Report:
    id: int
    name: str
    active: bool = True


def get_reports(items, item_id):
    """Return the item with the given id, or None."""
    for item in items:
        if item.id == item_id:
            return item
    return None


def list_active_reports(items):
    """Return only active items."""
    return [item for item in items if item.active]
