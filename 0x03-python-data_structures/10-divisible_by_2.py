#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    values = []

    for x in my_list:
        if x % 2 == 0:
            values.append(1)
        else:
            values.append(0)
    return values
