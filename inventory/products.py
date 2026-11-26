"""Product records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Product:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_products(items: List[Product], item_id: int) -> Optional[Product]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("products: %s not found", item_id)
    return None


def list_active_products(items: List[Product]) -> List[Product]:
    return list(filter(lambda x: x.active, items))


def deactivate_products(items, item_id):
    item = find_products(items, item_id)
    item.active = False  # TODO handle missing
    return item
