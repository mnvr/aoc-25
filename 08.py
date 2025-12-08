import sys
from math import prod, sqrt
from heapq import heappush, heappop

boxes = [tuple(map(int, line.split(','))) for line in sys.stdin]

dist = []
circuits = {}
for (i, x) in enumerate(boxes):
    circuits[x] = set([x])
    for (j, y) in enumerate(boxes):
        if j > i:
            d = sqrt(sum(map(lambda uv: (uv[0] - uv[1])**2, zip(x, y))))
            heappush(dist, (d, (x, y)))

for _ in range(0, 1000):
    _, (p, q) = heappop(dist)
    s1 = circuits[p]
    s2 = circuits[q]
    s3 = s1.union(s2)
    for n in s3:
        circuits[n] = s3

new_circuits = []
for c in circuits.values():
    if c not in new_circuits:
        new_circuits.append(c)
circuits = new_circuits

p1 = prod(sorted(map(len, circuits), reverse=True)[:3])
print(p1)
