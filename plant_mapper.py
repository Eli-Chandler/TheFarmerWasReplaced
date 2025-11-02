from __builtins__ import *
from utils import ensure_true


_EVERYTHING_MAP = [
    (Items.Hay, Entities.Grass),
    (Items.Wood, Entities.Tree),
    (Items.Carrot, Entities.Carrot),
    (Items.Pumpkin, Entities.Pumpkin),
    (Items.Power, Entities.Sunflower),
]


def _get_entry(t):
    for entry in _EVERYTHING_MAP:
        if t in entry:
            return entry
    ensure_true(False, ("Failed to find entry for type: ", t))


def get_item(t):
    entry = _get_entry(t)

    ensure_true(entry != None, ("Failed to find entry for type: ", t))
    ensure_true(entry[0] != None, ("Failed to find item for type: ", t))

    return entry[0]


def get_entity(t):
    entry = _get_entry(t)

    ensure_true(entry != None, ("Failed to find entry for type: ", t))
    ensure_true(entry[1] != None, ("Failed to find entity for type: ", t))

    return entry[1]


def get_all_items():
    items = []
    for entry in _EVERYTHING_MAP:
        items.append(entry[0])
    return items


def get_all_entities():
    entities = []
    for entry in _EVERYTHING_MAP:
        entities.append(entry[1])
    return entities
