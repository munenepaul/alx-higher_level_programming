#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    temp_value = 0
    for i in range(0, list_length):
        try:
            temp_value = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_value = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_value = 0
            print("division by 0")
        except IndexError:
            temp_value = 0
            print("out of range")
        finally:
            pass
        div.append(temp_value)
    return div
