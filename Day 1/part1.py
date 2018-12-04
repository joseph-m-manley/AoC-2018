#!/usr/bin/python

from math import fsum

def get_frequencies():
    with open('input.txt') as file:
        return [ int(x) for x in file.readlines() ]

def main():
    result = sum(get_frequencies())
    print(result)

if __name__ == '__main__':
    main()
