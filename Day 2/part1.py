#!/usr/bin/python3

def get_ids():
    with open('input.txt') as file:
        return file.readlines()


def try_add(id, two, three):
    two_added = False
    three_added = False

    for character in id:
        count = id.count(character)

        if count == 2 and not two_added:
            two.add(id)
            two_added = True
        elif count == 3 and not three_added:
            three.add(id)
            three_added = True


def checksum():
    ids = get_ids()

    two = set()
    three = set()

    for id in ids:
        try_add(id, two, three)

    print(len(two) * len(three))


if __name__ == '__main__':
    checksum()