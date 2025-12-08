import sys
from math import prod, sqrt
from heapq import heappush, heappop

boxes = [tuple(map(int, line.split(','))) for line in sys.stdin]
P1 = 10 if len(boxes) < 50 else 1000

dist = []
circuits = {}
for (i, x) in enumerate(boxes):
    circuits[x] = set([x])
    for (j, y) in enumerate(boxes):
        if j > i:
            d = sqrt(sum(map(lambda uv: (uv[0] - uv[1])**2, zip(x, y))))
            heappush(dist, (d, (x, y)))

def unique_circuits(circuits):
    uniq = []
    for c in circuits.values():
        if c not in uniq:
            uniq.append(c)
    return uniq

p1 = 0
i = 0
while len(unique_circuits(circuits)) > 1:
    i += 1
    _, pair = heappop(dist)
    (p, q) = pair
    p2 = p[0]*q[0]
    s1 = circuits[p]
    s2 = circuits[q]
    s3 = s1.union(s2)
    for n in s3:
        circuits[n] = s3

    if i == P1:
        uniq = unique_circuits(circuits)
        p1 = prod(sorted(map(len, uniq), reverse=True)[:3])

print(p1, p2)
