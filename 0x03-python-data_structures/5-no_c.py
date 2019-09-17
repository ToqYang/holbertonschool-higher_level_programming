#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    counter = 0
    new_string = []
    for x in my_string:
        new_string.insert(counter, x)
        if x == 'c':
            new_string.remove('c')
        if x == 'C':
            new_string.remove('C')
        counter += 1
    return (''.join(new_string))
