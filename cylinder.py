#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def cylinder(r, h, n):
    def circle():
        return math.pi * r * r

    if n == "full":
        return circle() * 2 + 2 * math.pi * r * h
    elif n == "side":
        return 2 * math.pi * r * h
    else:
        return 'Error'


if __name__ == '__main__':
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    square = input("Are you wanna get S full or side S? ")

    print(cylinder(radius, height, square))
