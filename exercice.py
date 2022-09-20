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


def format_number(number: float, num_decimal_digits: int) -> str:
    rounded_number = abs(round(number, num_decimal_digits))

    ## Split string
    # same thing as
    # whole_part, dec_part = str.split(".")
    whole_part = str()
    dec_part = str()
    whole_mode = True
    for num in str(rounded_number):
        if num == ".":
            whole_mode = False
            continue

        if whole_mode:
            whole_part += num
        else:
            dec_part += num

    ## Pad decimals if the last ones were 0
    # same thing as
    # dec_part.zfill(num_decimal_digits)
    dec_part += "0" * (num_decimal_digits - len(dec_part))

    ## Add spaces

    # For whole part,
    # single values are on the left `N NNN.`
    whole_part_fmt = str()
    for i, num in enumerate(reversed(whole_part)):
        whole_part_fmt = num + (" " if i % 3 == 0 and i != 0 else "") + whole_part_fmt

    # For decimal part,
    # single valeus are on the right `.NNN N`
    dec_part_fmt = str()
    for i, num in enumerate(dec_part):
        dec_part_fmt += (" " if i % 3 == 0 and i != 0 else "") + num

    # Add back neg sign if input number was neg
    return ("-" if number < 0 else "") + whole_part_fmt + "." + dec_part_fmt


def get_triangle(num_rows: int):
    rows: list[str] = []
    for i in range(1, num_rows + 1):
        rows.append("A" * (2 * i - 1))

    to_add = len(rows[-1])

    for i, row in enumerate(rows):
        rows[i] = "+" + f"{row:^{to_add}}" + "+"

    h_border = "+" * (to_add + 2)

    rows.insert(0, h_border)
    rows.append(h_border)

    return "\n".join(rows)


if __name__ == "__main__":
    print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

    print(format_number(-12345.678, 2))

    print(get_triangle(2))
    print(get_triangle(5))
