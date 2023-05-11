#!/usr/bin/python3

if __name__ == "__main__":
    from my_calculator import addition, subtraction, multiplication, division
    x = 10
    y = 5
    print("{} + {} = {}".format(x, y, addition(x, y)))
    print("{} - {} = {}".format(x, y, subtraction(x, y)))
    print("{} * {} = {}".format(x, y, multiplication(x, y)))
    print("{} / {} = {}".format(x, y, division(x, y)))
