#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    s = input("Enter string: ")
    return s


def test_input(s):
    if s.isdigit():
        return True
    else:
        return False


def str_to_int(s):
    return int(s)


def print_int(s):
    print(s, type(s))


if __name__ == "__main__":
    num = get_input()
    print(num, type(num))

    if test_input(num):
        str_to_int(num)
        print_int(str_to_int(num))
    else:
        print("Conversion not possible")
