#!/usr/bin/python3

def get_ids():
    with open('input.txt') as file:
        return file.readlines()

def fuzzify(id, before_skipped, after_skipped):
    return id[:before_skipped] + id[after_skipped:]

def find_match():
    ids = get_ids()

    for n in range(0, len(ids[0])):
        before_skipped = n
        after_skipped = n + 1

        s = set()

        for id in ids:
            fuzzy_id = fuzzify(id, before_skipped, after_skipped)

            if fuzzy_id in s:
                print(fuzzy_id)
                return
            else:
                s.add(fuzzy_id)

if __name__ == '__main__':
    find_match()