"""Discount records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Discount:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_discounts(items: List[Discount], item_id: int) -> Optional[Discount]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("discounts: %s not found", item_id)
    return None


def list_active_discounts(items: List[Discount]) -> List[Discount]:
    return list(filter(lambda x: x.active, items))


def deactivate_discounts(items, item_id):
    item = find_discounts(items, item_id)
    item.active = False  # TODO handle missing
    return item
