#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    num = int(input("Enter number: "))
    if num > 0:
        positive()
    elif num < 0:
        negative()
    else:
        print("It's zero")


def positive():
    print("Positive")


def negative():
    print("Negative")


if __name__ == '__main__':
    test()
