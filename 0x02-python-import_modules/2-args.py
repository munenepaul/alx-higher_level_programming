#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("{} arguments.".format(i))
    elif arg_count == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

        if arg_count >= 1:
            i = 1
            for arg in sys.argv[1:]:
                print("{}: {}".format(i, arg))
                i += 1
