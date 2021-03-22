#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List

class IllegalShopError(Exception):

    def __init__(self, price, message="Illegal Shop number"):
        self.price = price
        self.message = message
        super(IllegalShopError, self).__init__(message)

    def __str__(self):
        return f"{self.price} -> {self.message}"


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):

    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class markets:
    shop: str
    product: str
    price: float


@dataclass
class Staff:
    market: List[markets] = field(default_factory=lambda: [])

    def add(self, shop, product, price):

        if price < 0 or price > 999:
            raise IllegalShopError(price)

        self.market.append(
            markets(
                shop=shop,
                product=product,
                price=price
            )
        )

        self.market.sort(key=lambda markets: markets.shop)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Магазин",
                "Продукт",
                "Цена"
            )
        )
        table.append(line)

        # Вывести данные о всех товарах.
        for idx, markets in enumerate(self.market, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    markets.shop,
                    markets.product,
                    markets.price
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self, shop):
        parts = command.split(' ', maxsplit=1)
        shop = str(parts[1])
        count = 0
        result = []
        for markets in self.market:
            if product in markets.product:
                count += 1
                result.append(markets)
        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()

        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)

        self.market = []
        for markets_element in tree:
            shop, product, price = None, None, None
            for element in markets_element:
                if element.tag == 'product':
                    product = element.text
                elif element.tag == 'shop':
                    shop = element.text
                elif element.tag == 'price':
                    price = float(element.text)

                if shop is not None and product is not None \
                        and price is not None:
                    self.market.append(
                        markets(
                            shop=shop,
                            product=product,
                            price=price
                        )
                    )

    def save(self, filename):
        root = ET.Element('market')
        for markets in self.market:
            markets_element = ET.Element('markets')


            shop_element = ET.SubElement(markets_element, 'shop')
            shop_element.text = markets.shop

            product_element = ET.SubElement(markets_element, 'product')
            product_element.text = markets.product

            price_element = ET.SubElement(markets_element, 'price')
            price_element.text = str(markets.price)

            root.append(markets_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)