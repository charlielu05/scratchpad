import os
from string import punctuation
from dataclasses import dataclass
from typing import List


@dataclass
class Digit:
    value: int
    start: int
    end: int
    row: int


@dataclass
class Symbol:
    value: str
    row: int
    col: int


def check_for_symbols(digit: Digit, symbols: List[Symbol]) -> bool:
    # check if symbols are next to the digit

    # generate all x,y coordinates for the digit
    digit_coords = []
    for x in range(digit.row - 1, digit.row + 2):
        for y in range(digit.start - 1, digit.end + 1):
            digit_coords.append((x, y))

    if any((symbol.row, symbol.col) in digit_coords for symbol in symbols):
        return True
    else:
        return False


if __name__ == "__main__":
    # add up all the numbers in the input file that are next to a symbol
    # (. period does not count as symbol)

    # open text file
    with open("./test_input.txt", encoding="utf-8") as file:
        test_input = file.read().splitlines()
    # open full input text file
    with open("./full_input.txt", encoding="utf-8") as file:
        full_input = file.read().splitlines()

    # string chars of symbols
    symbols_set = set(punctuation) - set(".")

    # get the dimension of the input
    dim_x = len(full_input)
    dim_y = len(full_input[0])
    x_idx = 0
    y_idx = 0
    digits = []
    symbols = []

    while x_idx < dim_x:
        while y_idx < dim_y:
            # check current character is a symbol or digit
            if full_input[x_idx][y_idx].isdigit():
                # find the length of the digits
                length = 1
                while (
                    y_idx + length < dim_y
                    and full_input[x_idx][y_idx + length].isdigit()
                ):
                    length += 1

                digit_value = full_input[x_idx][y_idx : y_idx + length]
                digits.append(Digit(digit_value, y_idx, y_idx + length, x_idx))

                y_idx += length
            elif full_input[x_idx][y_idx] in symbols_set:
                symbols.append(Symbol(full_input[x_idx][y_idx], x_idx, y_idx))
                y_idx += 1
            else:
                y_idx += 1
        x_idx += 1
        y_idx = 0

    digits_with_symbols = [
        digit for digit in digits if check_for_symbols(digit, symbols)
    ]

    print(sum(int(digit.value) for digit in digits_with_symbols))

    # part two, find the two digits that are both connected to an asterisk symbol
    # and multiply their values
    # filter symbols list for only asterix symbol
    asterix = [symbol for symbol in symbols if symbol.value == "*"]
    # loop through individual asterix symbol and find the digits connected to it
    digits_with_asterix = [
        [digit for digit in digits if check_for_symbols(digit, [unique_asterix])]
        for unique_asterix in asterix
    ]
    # filter for only the digits that have two asterix symbols by checking length
    asterix_with_two_digits = [
        digit for digit in digits_with_asterix if len(digit) == 2
    ]

    # reduce function
    from functools import reduce

    def multiply(digits: List[Digit]):
        return reduce(lambda x, y: int(x.value) * int(y.value), digits)

    gear_ratios = [multiply(asterix_digit) for asterix_digit in asterix_with_two_digits]

    print(sum(gear_ratios))
