#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариаент 18
# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.
#Выполнить индивидуальное задание 2 лабораторной работы 9, использовав классы данных, а
#также загрузку и сохранение данных в формат XML.
#Изучить возможности модуля logging. Добавить для предыдущего задания вывод в файлы лога
#даты и времени выполнения пользовательской команды с точностью до миллисекунды
#Выполнить индивидуальное задание 2 лабораторной работы 14, оформив все функции
#программы в виде отдельного модуля. Разработанный модуль должен быть подключен в
#основную программу с помощью одного из вариантов команды  import .

from dataclasses import dataclass, field
import logging
import sys
import mod

import xml.etree.ElementTree as ET


# Класс пользовательского исключения в случае, если неверно
# введена цена продукта.



if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='market.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

    # Список товара.
    staff = Staff()

    # Организовать бесконечный цикл запроса команд.
    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                # Запросить данные о товаре.
                shop = input("Название магазина? ")
                product = input("Название товара? ")
                price = float(input("Стоимость товара в руб.? "))

                # Добавить.
                staff.add(shop, product, price)
                logging.info(
                    f"Добавлен товар: {product}, {shop}, "
                    f"поступивший по {price} цене."
                )

            elif command == 'list':
                # Вывести список.
                print(staff)
                logging.info("Отображен список товаров.")

            elif command.startswith('select '):

                parts = command.split(maxsplit=1)
                # Запросить товар.
                selected = staff.select(parts[1])

                parts = command.split(' ', maxsplit=2)

                shop = str(parts[1])

                # Инициализировать счетчик.
                count = 0

                # Вывести результаты запроса.
                if selected:
                    for count, markets in enumerate(selected, 1):
                        print(
                            '{:>4}: {}'.format(count, markets.product)
                        )
                    logging.info(
                        f"Найден {len(selected)} товар с "
                        f"ценой более {parts[1]} "
                    )
                else:
                    print("Товар не найден.")
                    logging.warning(
                        f"Товар с ценой {parts[1]} не найден."
                    )

            elif command.startswith('load '):
                # Разбить команду на части для выделения имени файла.
                parts = command.split(' ', maxsplit=1)

                # Прочитать данные из файла.
                staff.load(parts[1])
                logging.info(f"Загружены данные из файла {parts[1]}.")

            elif command.startswith('save '):
                # Разбить команду на части для выделения имени файла.
                parts = command.split(maxsplit=1)
                # Сохранить данные в файл.
                staff.save(parts[1])
                logging.info(f"Сохранены данные в файл {parts[1]}.")

            elif command == 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить продукт;")
                print("list - вывести список продуктов;")
                print("load <имя_файла> - загрузить данные из файла;")
                print("save <имя_файла> - сохранить данные в файл;")
                print("select <товар> - информация о товаре;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            else:
                raise UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
