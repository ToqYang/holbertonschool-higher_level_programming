#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    if my_list is None:
        return
    return list(map(lambda x: x * number, my_list))
