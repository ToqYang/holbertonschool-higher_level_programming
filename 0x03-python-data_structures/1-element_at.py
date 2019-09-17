#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list):
        return None
    for x in range(len(my_list)):
        if idx == x:
            return my_list[x]
