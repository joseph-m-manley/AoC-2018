#!/usr/bin/python

def get_changes():
    with open('input.txt') as file:
        return [ int(x) for x in file.readlines() ]

def main():
    changes = get_changes()

    current_freq = 0
    frequencies = { current_freq }

    while True:
        for change in changes:
            current_freq += change

            if current_freq in frequencies:
                print(current_freq)
                return
            else:
                frequencies.add(current_freq)


if __name__ == '__main__':
    main()