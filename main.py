from __builtins__ import *
from farming_utils import water_if_low
import w
from planting_functions import try_harvest, try_plant, register_observers
from position_utils import go_to

FOCUS = None


def do_plant():
    try_harvest()
    try_plant()
    water_if_low()


def main():
    go_to(0, 0)
    register_observers()
    while True:
        for i in range(12):  # type: ignore
            do_plant()
            w.wmove(North)
        w.wmove(East)


if __name__ == "__main__":
    main()
