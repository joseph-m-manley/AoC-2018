#!/usr/bin/python

def get_claims():
    with open('input.txt') as file:
        claims = file.readlines()
        return [ Claim(c) for c in claims ]


class Claim():
    def __init__(self, claim):
        self.claim = claim

        begin = claim.find('#') + 1
        end = claim.find('@')
        self.id = int(claim[ begin : end ].strip())

        begin = end + 1
        end = claim.find(':')
        origin = claim[ begin : end ].strip().split(',')
        self.left = int(origin[0])
        self.top = int(origin[1])

        begin = end + 1
        size = claim[ begin : ].strip().split('x')
        self.right = self.left + int(size[0])
        self.bottom = self.top + int(size[1])

    def __repr__(self):
        return self.claim

    def overlaps(self, other):
        if self.id == other.id:
            return False
        return (self.right > other.left and self.left < other.right and
                self.top < other.bottom and self.bottom > other.top)

    def try_get_overlapping_points(self, other):
        if not self.overlaps(other):
            return set()

        left = max(self.left, other.left)
        right = min(self.right, other.right)
        top = max(self.top, other.top)
        bottom = min(self.bottom, other.bottom)

        points = set()
        for x in range(left, right):
            for y in range(top, bottom):
                points.add( (x, y) )

        return points


def find_overlapping_claims():
    claims = get_claims()
    overlapping_points = set()

    while len(claims) > 0:
        claim = claims.pop()
        for other in claims:
            points = claim.try_get_overlapping_points(other)
            overlapping_points.update(points)

    print('Total overlapping area: {0} sqin'.format(len(overlapping_points)))


if __name__ == '__main__':
    find_overlapping_claims()