#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_product(products):
    prod = input("Введите название товара: ")
    shop = input("Введите название магазина: ")
    cost = float(input("Введите стоимость товара: "))
    product = {
        'product': prod,
        'shop': shop,
        'cost': cost
    }

    products.append(product)
    if len(products) > 1:
        products.sort(key=lambda item: item.get('shop', ''))


def product_list(products):

    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20
    )
    print(line)
    print(
        '| {:^25} | {:^15} | {:^14} |'.format(
            "Товар",
            "Магазин",
            "Стоимость"
        )
    )
    print(line)

    for product in products:
        print(
            '| {:^25} | {:^15} | {:^14} |'.format(
                product.get('product', ''),
                product.get('shop', ''),
                product.get('cost', 0)
            )
        )
    print(line)


def select(products):
    sel_shop = input("Введите магазин: ")

    n = 0
    for product in products:
        if product.get('shop', '') == sel_shop:
            print(
                '| {:^25} | {:^15} | {:^14} |'.format(
                    product.get('product', ''),
                    product.get('shop', ''),
                    product.get('cost', 0)
                )
            )
            n += 1
    if n == 0:
        print("Магазин не найден!")


def get_help():
    print("Список команд:\n")
    print("add - добавить информацию о товаре;")
    print("list - вывести список товаров;")
    print("select - запросить товары из одного магазина;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def error(command):
    print(f"Неизвестная команда {command}", file=sys.stderr)


def main():
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add_product(products)

        elif command == 'list':
            product_list(products)

        elif command == 'select':
            select(products)

        elif command == 'help':
            get_help()

        else:
            error(command)


if __name__ == '__main__':
    main()
