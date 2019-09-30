#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    data = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            data += 1
        except:
            pass
    print()
    return data
