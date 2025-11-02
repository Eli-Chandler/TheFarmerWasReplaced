from __builtins__ import *
from farming_utils import till_if_needed
from planting_functions import wait_harvest
from position_utils import go_to


def turbo_cactus(stop_condition_function=None):
    clear()

    acceptable_values_rows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    acceptable_values_cols = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    while stop_condition_function == None or not stop_condition_function():
        for x in range(10):
            for y in range(10):
                go_to(x, y)
                size = min(
                    acceptable_values_rows[y],
                    acceptable_values_cols[x],
                )

                size =_plant_cactus(size, min(x, y))
                quick_print("Planted", size)
                acceptable_values_rows[y] = max(acceptable_values_rows[y], size)
                acceptable_values_cols[x] = max(acceptable_values_cols[x], size)
                acceptable_values_rows[y+1] = max(acceptable_values_rows[y+1], size)
                acceptable_values_cols[x+1] = max(acceptable_values_cols[x+1], size)

        wait_harvest()

def _plant_cactus(min_size, max_size):
    till_if_needed()
    plant(Entities.Cactus)

    while measure() < min_size or measure() > max_size:
        harvest()
        plant(Entities.Cactus)

    return measure()

if __name__ == "__main__":
    turbo_cactus()