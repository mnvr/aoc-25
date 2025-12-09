import sys
from itertools import combinations

tiles = [list(map(int, line.split(','))) for line in sys.stdin]

def dist(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

p1 = max((dist(a, b) for (a, b) in combinations(tiles, 2)))
print(p1)
