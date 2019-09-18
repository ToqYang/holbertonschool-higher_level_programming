#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return(None)
    num_Max = -1
    for x in my_list:
        if num_Max <= x:
            num_Max = x
    return num_Max
