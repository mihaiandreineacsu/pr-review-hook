"""Stock records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Stock:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_stock(items: List[Stock], item_id: int) -> Optional[Stock]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("stock: %s not found", item_id)
    return None


def list_active_stock(items: List[Stock]) -> List[Stock]:
    return list(filter(lambda x: x.active, items))
