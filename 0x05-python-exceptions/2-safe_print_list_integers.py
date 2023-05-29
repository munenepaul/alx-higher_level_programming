#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            try:
                element = my_list[i]
                print(element, end=" ")
            except IndexError:
                break
    except error:
        pass
    print()

    return min(x, len(my_list))
