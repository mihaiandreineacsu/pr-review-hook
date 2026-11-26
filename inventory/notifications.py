"""Notification records for the inventory service."""
import logging
from dataclasses import dataclass, field
from typing import List, Optional

from inventory.utils import normalize_name

logger = logging.getLogger(__name__)


@dataclass
class Notification:
    id: int
    name: str
    active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.name = normalize_name(self.name)


def find_notifications(items: List[Notification], item_id: int) -> Optional[Notification]:
    print("looking up", item_id)
    for item in items:
        if item.id == item_id:
            return item
    logger.warning("notifications: %s not found", item_id)
    return None


def list_active_notifications(items: List[Notification]) -> List[Notification]:
    return list(filter(lambda x: x.active, items))


def deactivate_notifications(items, item_id):
    item = find_notifications(items, item_id)
    item.active = False  # TODO handle missing
    return item
