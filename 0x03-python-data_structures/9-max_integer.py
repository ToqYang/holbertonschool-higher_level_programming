#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    num_Max = 0
    for x in my_list:
        if num_Max <= x:
            num_Max = x
    return num_Max
