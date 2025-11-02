from __builtins__ import *
from farming_utils import till_if_needed
from position_utils import go_to


def turbo_power(stop_condition_function=None):
    _setup()
    while stop_condition_function == None or not stop_condition_function():
        for x in range(10):
            go_to(x, 1)
            plant(Entities.Sunflower)
        for x in range(1):
            go_to(x, 1)
            harvest()

def _setup():
    for x in range(9):
        go_to(x, 0)
        _plant_min_flower()

MIN_FLOWER = 7

def _plant_min_flower():
    till_if_needed()
    plant(Entities.Sunflower)
    while measure() > MIN_FLOWER:
        harvest()
        plant(Entities.Sunflower)

if __name__ == '__main__':
    turbo_power()