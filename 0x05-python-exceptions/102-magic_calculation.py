#!/usr/bin/python3
def magic_calculation(a, b):
    returnvalue = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                returnvalue += a ** b / i
        except Exception:
            returnvalue = b + a
            break
        return returnvalue
