from __builtins__ import *
from farming_utils import water_if_low, till_if_needed
from position_utils import go_to_tuple


def turbo_polyculture(stop_condition_function=None):
    companion_type, pos = _polyculture_plant(Entities.Tree, (0, 0))
    while stop_condition_function == None or not stop_condition_function():
        companion_type, pos = _polyculture_plant(companion_type, pos)

def _polyculture_plant(plant_type, pos_tuple):
    go_to_tuple(pos_tuple)
    while get_entity_type() != None and not can_harvest():
        if num_items(Items.Fertilizer) > 0:
            use_item(Items.Fertilizer)
    harvest()
    water_if_low()
    till_if_needed()
    plant(plant_type)
    return get_companion()

if __name__ == '__main__':
    turbo_polyculture(None)