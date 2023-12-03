from typing import Iterable
import re

test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def find_digits(input_str: str, mapping: Iterable):
    left = None
    right = None

    left_idx = 0

    for i, value in enumerate(input_str):
        if value in mapping:
            left = value
            left_idx = i
            break

    # remove all strings that we have searched already
    input_str_remaining = input_str[left_idx:]
    for i, value in enumerate(input_str_remaining[::-1]):
        if value in mapping:
            right = value
            break

    return (left, right)


if __name__ == "__main__":
    with open("./calibration_input.txt", "r", encoding="utf-8") as calibration_file:
        calibration_data = calibration_file.read().split("\n")

    results = [find_digits(input, ints) for input in test_data]
    results_sum = sum((10 * int(x) + int(y)) for x, y in results)

    results_aoc = [find_digits(input, ints) for input in calibration_data]
    result_aoc_sum = sum((10 * int(x) + int(y)) for x, y in results_aoc)

    # part two
    p2_test_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    reversed_mapping = dict(
        zip([x[::-1] for x in number_mapping.keys()], number_mapping.values())
    )

    numbers = "(one|two|three|four|five|six|seven|eight|nine|[0-9])"
    reversed_numbers = "one|two|three|four|five|six|seven|eight|nine"[::-1]
    reverse_regex = f"({reversed_numbers}|[0-9])"

    def part_two_function(input_data: Iterable):
        left_side = (re.findall(numbers, input_data))[0]

        ls_cleanup_func = lambda x: int(x) if x.isdigit() else number_mapping.get(x)

        left_side_number = ls_cleanup_func(left_side)

        right_side = (re.findall(reverse_regex, input_data[::-1]))[0]

        rs_cleanup_func = lambda x: int(x) if x.isdigit() else reversed_mapping.get(x)

        right_side_number = rs_cleanup_func(right_side)

        return 10 * left_side_number + right_side_number

    # _, test_p2_result = part_two_function(p2_test_data)
    # assert test_p2_result == 281

    # full_data, sum_full_data = part_two_function(calibration_data)

    test_overlap = "oneight"

    assert part_two_function(test_overlap) == 18

    part_two_result = sum(
        part_two_function(input_string) for input_string in calibration_data
    )
