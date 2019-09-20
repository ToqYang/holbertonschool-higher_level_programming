#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    copy_Dic = {}
    copy_Dic = a_dictionary.copy()
    for x in a_dictionary:
        copy_Dic[x] *= 2
    return copy_Dic
