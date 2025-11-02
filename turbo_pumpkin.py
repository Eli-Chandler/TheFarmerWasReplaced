from __builtins__ import *
from farming_utils import till_if_needed, water_if_low
from position_utils import find_nearest_position, go_to_tuple
from utils import always_false, copy_list


def turbo_pumpkin(stop_condition_function=None):
    while stop_condition_function == None or not stop_condition_function():
        check_curr = set()
        for x in range(6):
            for y in range(6):
                check_curr.add((x, y))

        while len(check_curr) > 0:
            check_next = set()
            while len(check_curr) > 0:

                nearest = find_nearest_position(check_curr)
                go_to_tuple(nearest)
                water_if_low()

                if get_entity_type() == Entities.Pumpkin and can_harvest():
                    check_curr.remove(nearest)
                    continue
                _plant_pumpkin()
                check_curr.remove(nearest)
                check_next.add(nearest)
            check_curr = check_next

        harvest()

def _plant_pumpkin():
    quick_print("Planting pumpkin")
    till_if_needed()
    plant(Entities.Pumpkin)

if __name__ == '__main__':
    turbo_pumpkin()