#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_bill(name: str, data: list[tuple[str, int, float]]):
    INDEX_NAME = 0
    INDEX_QUANTITY = 1
    INDEX_PRICE = 2

    # Calculate qty
    sous_total = sum([i[INDEX_QUANTITY] * i[INDEX_PRICE] for i in data])
    taxes = sous_total * 0.15
    total = sous_total + taxes

    # What will be shown
    to_display: list[list[str]] = [
        [name, ""],
        ["SOUS TOTAL", f"{sous_total:>10.2f} $"],
        ["TAXES", f"{taxes:>10.2f} $"],
        ["TOTAL", f"{total:>10.2f} $"],
    ]

    # Find how much we need to pad the title
    max_length = max([len(items[0]) for items in to_display])
    for items in to_display:
        items[0] += " " * (max_length - len(items[0]))

    return "\n".join([items[0] + items[1] for items in to_display])


def format_number(number, num_decimal_digits):
    return ""


def get_triangle(num_rows):
    return ""


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
