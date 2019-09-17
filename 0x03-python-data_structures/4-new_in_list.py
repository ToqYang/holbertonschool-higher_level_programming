#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list.copy(my_list)
    lenlist = len(copy_list)
    if my_list is None:
        return
    if idx < 0 or idx > lenlist:
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
