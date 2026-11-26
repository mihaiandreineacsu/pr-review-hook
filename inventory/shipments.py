"""Shipment records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Shipment:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_shipments(items: List[Shipment], item_id: int) -> Optional[Shipment]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("shipments: %s not found", item_id)
    return None


def list_active_shipments(items: List[Shipment]) -> List[Shipment]:
    return list(filter(lambda x: x.active, items))


def deactivate_shipments(items, item_id):
    item = find_shipments(items, item_id)
    item.active = False  # TODO handle missing
    return item


# old version, keep for now
# def legacy_lookup(items, item_id):
#     return [x for x in items if x.id == item_id][0]
