from __builtins__ import *
from farming_utils import till_if_needed, get_plantable_items_ordered_by_count
from plant_mapper import get_item
from position_utils import x_mod, y_mod, get_pos_tuple
from utils import get_dictionary_values
from w import wplant, register_on_move_observer, register_on_plant_observer


def default_try_harvest():
    if can_harvest():
        harvest()
        return True
    return False


# == HAY ==


def try_plant_hay():
    wplant(Entities.Grass)
    return True


def try_harvest_hay():
    return default_try_harvest()


# == CARROT ==


def try_plant_carrot():
    till_if_needed()
    wplant(Entities.Carrot)
    return True


def try_harvest_carrot():
    return default_try_harvest()


# == WOOD ==


def try_plant_wood():
    if (x_mod(2) == 0 and y_mod(2) == 0) or (x_mod(2) == 1 and y_mod(2) == 1):
        wplant(Entities.Tree)
        return True
    return False


def try_harvest_wood():
    return default_try_harvest()


# == PUMPKIN ==

_PUMPKIN_POSITIONS = {}
_PUMPKINS_ALIVE_COUNT = 0


def all_pumpkins_alive():
    return _PUMPKINS_ALIVE_COUNT >= 6 * 6


def try_plant_pumpkin():
    if get_pos_x() >= 6 or get_pos_y() >= 6:
        return False
    till_if_needed()
    wplant(Entities.Pumpkin)
    return True


def try_harvest_pumpkin():
    if _PUMPKINS_ALIVE_COUNT >= 6 * 6 and can_harvest():
        harvest()
        return True
    return False


def no_op_harvest():
    return False


def pumpkin_observe_on_move():
    global _PUMPKINS_ALIVE_COUNT
    x = get_pos_x()
    y = get_pos_y()

    if (x, y) not in _PUMPKIN_POSITIONS:
        _PUMPKIN_POSITIONS[(x, y)] = False

    if get_entity_type() == Entities.Pumpkin and can_harvest():
        if not _PUMPKIN_POSITIONS[(x, y)]:
            _PUMPKIN_POSITIONS[(x, y)] = True
            _PUMPKINS_ALIVE_COUNT += 1
    else:
        if _PUMPKIN_POSITIONS[(x, y)]:
            _PUMPKIN_POSITIONS[(x, y)] = False
            _PUMPKINS_ALIVE_COUNT -= 1


## == SUNFLOWER ==

from __builtins__ import measure, harvest

_SUNFLOWER_PETALS = {}


def add_sunflower_petals():
    # Only measure if we're actually on a sunflower
    if get_entity_type() != Entities.Sunflower:
        # If there's no sunflower here but we have it tracked, remove it
        if get_pos_tuple() in _SUNFLOWER_PETALS:
            _SUNFLOWER_PETALS.pop(get_pos_tuple())
        return

    petals = measure()
    _SUNFLOWER_PETALS[get_pos_tuple()] = petals


def try_plant_sunflower():
    if get_pos_x() < 6 and get_pos_y() < 6:
        return False
    quick_print("SUNFLOWER PETALS:", _SUNFLOWER_PETALS)
    if num_items(Items.Power) > 100 or len(_SUNFLOWER_PETALS) >= 10:
        return False
    till_if_needed()
    wplant(Entities.Sunflower)
    add_sunflower_petals()
    return True


def try_harvest_sunflower():
    add_sunflower_petals()
    if not can_harvest():
        return False

    if len(_SUNFLOWER_PETALS) < 10:  # type: ignore
        quick_print("Note enough sunflowers to harvest.")
        return False
    petals = measure()

    if (
        petals < max(get_dictionary_values(_SUNFLOWER_PETALS))
        and len(_SUNFLOWER_PETALS) <= 10
    ):
        return False
    harvest()
    _SUNFLOWER_PETALS.pop(get_pos_tuple())
    return True


# Just to catch any unregistered sunflowers
def sunflower_observe_move():
    add_sunflower_petals()


# == UTILS ==

_ITEM_PLANT_FUNCTION_MAP = {
    Items.Hay: try_plant_hay,
    Items.Carrot: try_plant_carrot,
    Items.Wood: try_plant_wood,
    Items.Pumpkin: try_plant_pumpkin,
    Items.Power: try_plant_sunflower,
}

_ENTITY_HARVEST_FUNCTION_MAP = {
    Entities.Grass: try_harvest_hay,
    Entities.Carrot: try_harvest_carrot,
    Entities.Tree: try_harvest_wood,
    Entities.Pumpkin: try_harvest_pumpkin,
    Entities.Sunflower: try_harvest_sunflower,
    Entities.Dead_Pumpkin: no_op_harvest,
    None: no_op_harvest,
}


def get_plant_function_for_item(item):
    return _ITEM_PLANT_FUNCTION_MAP[item]


def get_harvest_function_for_entity(entity):
    return _ENTITY_HARVEST_FUNCTION_MAP[entity]


def register_observers():
    register_on_move_observer(pumpkin_observe_on_move)
    register_on_move_observer(sunflower_observe_move)


def try_harvest():
    entity_type = get_entity_type()
    if entity_type == None:
        quick_print("Warning: try_harvest called but no entity present")
        return False
    quick_print("Trying to harvest", entity_type)

    harvest_function = get_harvest_function_for_entity(entity_type)
    return harvest_function()


def try_plant(item=None, priorities=None):
    if priorities == None:
        priorities = get_plantable_items_ordered_by_count()

    if item != None:
        quick_print("Trying to plant", item)
        plant_function = get_plant_function_for_item(get_item(item))
        if plant_function():
            return True
        quick_print("Failed to plant", item)

    for priority_item in priorities:
        if item == priority_item:
            continue
        quick_print("Trying to plant", item)
        plant_function = get_plant_function_for_item(priority_item)

        if plant_function():
            return True
        quick_print("Failed to plant", priority_item)
    return False

def wait_harvest():
    while get_entity_type() != None and not can_harvest():
        pass
    harvest()