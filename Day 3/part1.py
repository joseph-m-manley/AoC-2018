#!/usr/bin/python

class Claim():
    def __init__(self, claim):
        self.string = claim

        begin = claim.find('#') + 1
        end = claim.find('@')
        self.id = claim[ begin : end ].strip()

        begin = end + 1
        end = claim.find(':')
        origin = claim[ begin : end ].strip().split(',')
        self.from_left = int(origin[0])
        self.from_top = int(origin[1])

        begin = end + 1
        size = claim[ begin : ].strip().split('x')
        self.width = int(size[0])
        self.height = int(size[1])

        self.sqin = self.width * self.height

    def __str__(self):
        return self.string


def get_claims():
    with open('input.txt') as file:
        claims = file.readlines()
        return [ Claim(c) for c in claims ]


def find_overlapping_claims():
    claims = get_claims()
    sorted_claims = sorted(claims, key=(lambda c: c.from_left))

    # add up expected total sqin
    expected_sqin = sum([ c.sqin for c in claims ])
    print(expected_sqin)

    # less actual sqin
    raise NotImplementedError('Not finished with this problem')


if __name__ == '__main__':
    find_overlapping_claims()