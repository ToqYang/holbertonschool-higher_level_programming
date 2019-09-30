#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for a in range(0, x):
            print("{}".format(my_list[a]), end="")
        print()
        a += 1
    except:
        print()
        pass
    return a
