#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            try:
                element = my_list[i]
                print(element, end=" ")
            except IndexError:
                break
    except:
        pass
    print()
    return min(x, len(my_list))
