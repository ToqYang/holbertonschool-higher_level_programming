#!/usr/bin/python3
def element_at(my_list, idx):
    lenlist = len(my_list)
    if idx < 0 or idx > lenlist:
        return None
    return my_list[idx]
