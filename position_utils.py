from __builtins__ import *
import w
from utils import ensure_true

GRID = 12

def get_pos_tuple():
    return (get_pos_x(), get_pos_y())

def x_mod(n=2):
    return get_pos_x() % n

def y_mod(n=2):
    return get_pos_y() % n

def go_to_tuple(pos):
    go_to(pos[0], pos[1])

def go_to(x, y):
    cx, cy = get_pos_tuple()

    while cx != x:
        dx_east  = (x - cx) % GRID
        dx_west  = (cx - x) % GRID
        if dx_east <= dx_west:
            w.wmove(East)
            cx = (cx + 1) % GRID
        else:
            w.wmove(West)
            cx = (cx - 1) % GRID

    while cy != y:
        dy_south = (y - cy) % GRID
        dy_north = (cy - y) % GRID
        if dy_south <= dy_north:
            w.wmove(South)
            cy = (cy + 1) % GRID
        else:
            w.wmove(North)
            cy = (cy - 1) % GRID


def find_nearest_position(positions, start_pos=None):
    ensure_true(positions != None, "positions must not be None")
    ensure_true(len(positions) > 0, "positions must contain at least one position")

    if start_pos == None:
        start_pos = get_pos_tuple()
    nearest_pos = None
    nearest_distance = None
    for pos in positions:
        distance = abs(pos[0] - start_pos[0]) + abs(pos[1] - start_pos[1])
        if nearest_distance == None or distance < nearest_distance:
            nearest_distance = distance
            nearest_pos = pos
    return nearest_pos

def go_to_nearest(positions):
    nearest_pos = find_nearest_position(positions)
    if nearest_pos != None:
        go_to(nearest_pos[0], nearest_pos[1])
        return True
    return False