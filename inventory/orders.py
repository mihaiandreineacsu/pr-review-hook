"""Order records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Order:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_orders(items: List[Order], item_id: int) -> Optional[Order]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("orders: %s not found", item_id)
    return None


def list_active_orders(items: List[Order]) -> List[Order]:
    return list(filter(lambda x: x.active, items))
