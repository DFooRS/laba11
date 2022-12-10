#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiple():
    global result

    while True:
        n = float(input("Enter number: "))
        if n != 0:
            result *= n
        else:
            return result


if __name__ == '__main__':
    result = 1
    print(multiple())
