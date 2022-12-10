#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    def circle():
        return math.pi * r * r

    n = input("Are you wanna get S full or side S? ")

    if n == "full":
        print(circle() * 2 + 2 * math.pi * r * h)
    elif n == "side":
        print(2 * math.pi * r * h)
    else:
        print('Enter "full" or "side"! ', file=sys.stderr)


if __name__ == '__main__':
    cylinder()
