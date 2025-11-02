from __builtins__ import *
from farming_utils import till_if_needed
from position_utils import go_to


def turbo_cactus(stop_condition_function=None):
    clear()
    while stop_condition_function == None or not stop_condition_function():
        for x in range(10):
            for y in range(10):
                go_to(x, y)
                plant(min(x, y) + 1)

def _plant_cactus(size):
    till_if_needed()
    plant(Entities.Cactus)
    while measure() != size:
        harvest()
        plant(Entities.Sunflower)