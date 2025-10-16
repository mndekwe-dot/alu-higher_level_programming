#!/usr/bin/python3
def uppercase(str):

    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            char_code = ord(c) - 32
        else:
            char_code = ord(c)

        print("{}".format(chr(char_code)), end="")

    print()

