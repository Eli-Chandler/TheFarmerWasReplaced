from __builtins__ import *

def copy_list(list):
    new_list = []
    for item in list:
        new_list.append(item)
    return new_list


def is_in_list(i, list):
    for item in list:
        if item == i:
            return True
    return False


def crash():
    return 1 / 0

def ensure_true(condition, message_tuple):
    if condition != True:
        quick_print(message_tuple)
        return crash()
    return None

def get_dictionary_values(dictionary):
    values = []
    for key in dictionary:
        quick_print(key)
        values.append(dictionary[key])
    return values

def always_true():
    return True

def always_false():
    return False