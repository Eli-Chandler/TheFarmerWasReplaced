from __builtins__ import *

_move_observers = []


def register_on_move_observer(callback):
    _move_observers.append(callback)


def wmove(direction):
    move(direction)
    for callback in _move_observers:
        callback()


_plant_observers = []


def register_on_plant_observer(callback):
    _plant_observers.append(callback)


def wplant(entity):
    plant(entity)
    for callback in _plant_observers:
        callback()
