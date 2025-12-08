import sys
from math import prod, dist
from itertools import combinations

boxes = [tuple(map(int, line.split(','))) for line in sys.stdin]
P1 = 10 if len(boxes) < 50 else 1000

ds = list(sorted(combinations(boxes, 2), key=lambda p: dist(*p)))
circuits = {b: set([b]) for b in boxes}

p1 = 0
V = len(boxes) - 1
i = 0
while i < V:
    p, q = ds[i]
    i += 1
    p2 = p[0]*q[0]
    s1 = circuits[p]
    s2 = circuits[q]

    # MST has V-1 edges, increment if we're adding redundant ones.
    if p in s2 or q in s1:
        V += 1

    s3 = s1.union(s2)
    for n in s3:
        circuits[n] = s3

    if i == P1:
        uniq = []
        for c in circuits.values():
            if c not in uniq:
                uniq.append(c)
        p1 = prod(sorted(map(len, uniq), reverse=True)[:3])

print(p1, p2)
