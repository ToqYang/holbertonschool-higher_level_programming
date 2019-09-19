#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    other_List = my_list.copy()
    for x in range(len(other_List)):
        if other_List[x] == search:
            other_List[x] = replace
    return other_List
