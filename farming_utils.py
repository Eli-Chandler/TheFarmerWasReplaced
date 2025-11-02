import plant_mapper
from __builtins__ import *


def till_if_needed():
    if get_ground_type() != Grounds.Soil:
        till()
        return True
    return False


def water_if_low():
    if num_items(Items.Water) > 0 and get_water() * 100 < num_items(Items.Water):
        use_item(Items.Water)
        return True
    return False


def get_lowest_plantable_item(items=None):
    if items == None:
        items = plant_mapper.get_all_items()

    lowest_plant = None
    lowest_count = None

    for item in items:
        count = num_items(item)
        if lowest_count == None or count < lowest_count:
            lowest_count = count
            lowest_plant = item

    return lowest_plant


def get_plantable_items_ordered_by_count(items=None):
    if items == None:
        items = plant_mapper.get_all_items()

    ordered = []
    while len(items) > 0:
        lowest_plant = get_lowest_plantable_item(items)
        ordered.append(lowest_plant)
        items.remove(lowest_plant)

    return ordered
