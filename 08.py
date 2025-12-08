import sys
from math import prod, sqrt

boxes = [tuple(map(int, line.split(','))) for line in sys.stdin]

dist = {}
for (i, x) in enumerate(boxes):
    for (j, y) in enumerate(boxes):
        if j > i:
            d = sqrt(sum(map(lambda uv: (uv[0] - uv[1])**2, zip(x, y))))
            dist[(x, y)] = d

circuits = []
for _ in range(0, 1000):
    min_dist = int(1e9)
    min_dist_pair = None
    for key, value in dist.items():
        if value < min_dist:
            min_dist = value
            min_dist_pair = key
    del dist[min_dist_pair]
    pair = min_dist_pair
    new_circuit = set([pair[0], pair[1]])
    for c in circuits:
        if pair[0] in c or pair[1] in c:
            new_circuit = new_circuit.union(c)
    circuits = [c for c in circuits if not (pair[0] in c or pair[1] in c)]
    circuits.append(new_circuit)

p1 = prod(sorted(map(len, circuits), reverse=True)[:3])
print(p1)
