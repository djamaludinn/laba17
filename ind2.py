#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Выполнить индивидуальное задание 1 лабораторной работы 13, оформив все классы программы
#в виде отдельного пакета. Разработанный пакет должен быть подключен в основную программу с
#помощью одного из вариантов команды  import . Настроить соответствующим образом
#переменную  __all__  в файле  __init__.py  пакета. Номер варианта уточнить у преподавателя.


from ind2 import Triangle


if __name__ == '__main__':
    r1 = Triangle(first=7, second=12, third=5, square=13)
    print(f"r1 = {r1}")

    r2 = Triangle(first=9, second=6, third=8, square=16)
    print(f"r2 = {r2}")

    print(f"S1 < S2: {r1 < r2}")
    print(f"S1 > S2: {r1 > r2}")
    print(f"S1 <= S2: {r1 <= r2}")
    print(f"S1 >= S2: {r1 >= r2}")
    print(f"S1 = S2: {r1 == r2}")
    print(f"S1 != S2: {r1 != r2}")

    print(f"S1 + S2: {r1 + r2}")
    print(f"S1 - S2: {r1 - r2}")
    print(f"S1 * S2: {r1 * r2}")
    print(f"S1 / S2: {r1 / r2}")