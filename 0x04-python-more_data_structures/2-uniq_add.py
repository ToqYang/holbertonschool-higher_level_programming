#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    set_uno = set(my_list)
    result = 0
    for x in set_uno:
        result += x
    return result
