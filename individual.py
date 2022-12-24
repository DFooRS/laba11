#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_product():
    """
    Ввод информации о товарах.
    """
    prod = input("Введите название товара: ")
    shop = input("Введите название магазина: ")
    cost = float(input("Введите стоимость товара: "))

    return {
        'product': prod,
        'shop': shop,
        'cost': cost
    }


def product_list(products):
    """
    Вывод списка товаров
    """
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


def select(products, shop):
    """
    Выбрать товары из конкретного магазина.
    """
    result = []
    for product in products:
        if product.get('shop', '') == shop:
            result.append(product)
    return result


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
    """
    Главная функция программы.
    """
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = add_product()
            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('shop', ''))

        elif command == 'list':
            product_list(products)

        elif command == 'select':
            sel_shop = input("Введите магазин: ")
            selected = select(products, sel_shop)
            product_list(selected)

        elif command == 'help':
            get_help()

        else:
            error(command)


if __name__ == '__main__':
    main()
