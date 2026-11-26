"""Supplier records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Supplier:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_suppliers(items: List[Supplier], item_id: int) -> Optional[Supplier]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("suppliers: %s not found", item_id)
    return None


def list_active_suppliers(items: List[Supplier]) -> List[Supplier]:
    return list(filter(lambda x: x.active, items))
