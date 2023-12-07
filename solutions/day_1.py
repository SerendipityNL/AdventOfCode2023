import re
from helpers import get_input


# Part 1
def calculate_line_numbers(lines):

    numbers = []

    for line in lines:

        first_number = re.search(r"(\d)", line)[1]

        number = first_number + re.search(r"(\d)", line[::-1])[1]

        numbers.append(int(number))

    return sum(numbers)


# Part 2
stringDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def parse_lines(lines):

    return [re.sub(f"(?=({'|'.join(stringDict.keys())}))", string_to_number, line) for line in lines]


def string_to_number(regex_match):

    return stringDict[regex_match.group(1)]


print(calculate_line_numbers(get_input(1)))
print(calculate_line_numbers(parse_lines(get_input(1))))
