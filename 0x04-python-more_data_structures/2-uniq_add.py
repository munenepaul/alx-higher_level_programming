#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0

    unique_elements = []
    res = 0

    for num in my_list:
        if num not in unique_elements:
            unique_elements.append(num)
            res += num
    return res
