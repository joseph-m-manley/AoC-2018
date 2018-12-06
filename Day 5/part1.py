#!/usr/bin/python

import string

def get_polymer():
    with open('input.txt') as file:
        return list(file.read())


def can_react(polymer, index):
    first = polymer[index]
    second = polymer[index + 1]
    return first == second.swapcase()


def react(polymer, index):
    polymer.pop(index + 1)
    polymer.pop(index)


def try_react(polymer):
    for index in range(0, len(polymer) - 1):
        if can_react(polymer, index):
            react(polymer, index)
            return True

    return False


def collapse_polymer(polymer):
    while try_react(polymer):
        pass


def find_natural_collapsed_length():
    polymer = get_polymer()
    collapse_polymer(polymer)
    print('Natural collapsed length: {0}'.format(len(polymer)))


def find_minimum_possible_collapsed_length():
    polymer = get_polymer()
    results = list()

    for letter in string.ascii_lowercase:
        filtered_polymer = list(filter(lambda x: x.lower() != letter, polymer))
        collapse_polymer(filtered_polymer)

        length = len(filtered_polymer)
        results.append(length)
        print('Length after removing {0}: {1}'.format(letter, length))

    print(min(results))


if __name__ == '__main__':
    # print('Part 1')
    # find_natural_collapsed_length()

    print('Part 2')
    find_minimum_possible_collapsed_length()

