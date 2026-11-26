"""Customer records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Customer:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_customers(items: List[Customer], item_id: int) -> Optional[Customer]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("customers: %s not found", item_id)
    return None


def list_active_customers(items: List[Customer]) -> List[Customer]:
    return list(filter(lambda x: x.active, items))


# old version, keep for now
# def legacy_lookup(items, item_id):
#     return [x for x in items if x.id == item_id][0]
