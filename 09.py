import sys
from itertools import combinations
from collections import defaultdict
from random import randrange

tiles = [list(map(int, line.split(','))) for line in sys.stdin]

def dist(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

ds = ((dist(a, b), (a, b)) for (a, b) in combinations(tiles, 2))
ds = list(sorted(ds, reverse=True))

vertical_lines = defaultdict(list)
horizontal_lines = defaultdict(list)
max_x, max_y = 0, 0
for (x, y), (u, v) in zip(tiles, tiles[1:] + [tiles[0]]):
    max_x, max_y = max(max_x, x, u), max(max_y, y, v)
    if x == u:
        vertical_lines[x].append((min(y, v), max(y, v)))
    else:
        horizontal_lines[y].append((min(x, u), max(x, u)))

hx = defaultdict(set)
for y in horizontal_lines:
    s = set()
    for a, b in horizontal_lines[y]:
        for x in range(a, b + 1):
            s.add(x)
    hx[y] = s

vy = defaultdict(set)
for x in vertical_lines:
    s = set()
    for a, b in vertical_lines[x]:
        for y in range(a, b + 1):
            s.add(y)
    vy[x] = s

def is_point_on_boundary(x, y):
    return x in hx[y] or y in vy[x]

def is_point_inside_or_boundary(x, y):
    if is_point_on_boundary(x, y):
        return True

    for u in range(x, 0, -1):
        if is_point_on_boundary(u-1, y):
            break
    else:
        return False

    for u in range(x+1, max_x+1):
        if is_point_on_boundary(u, y):
            break
    else:
        return False

    for v in range(y, 0, -1):
        if is_point_on_boundary(x, v-1):
            break
    else:
        return False

    for v in range(y+1, max_y+1):
        if is_point_on_boundary(x, v):
            break
    else:
        return False

    return True

def vis():
    print("012345678901234")
    for y in range(0, max_y + 3):
        print(f"{y % 10}", end='')
        for x in range(0, max_x + 3):
            if is_point_on_boundary(x, y):
                print('#', end='')
            elif is_point_inside_or_boundary(x, y):
                print('\033[37m#\033[0m', end='')
            else:
                print('.', end='')
        print()
    print()

if len(ds) < 100:
    vis()

def check_border(x, y, u, v):
    x1, y1 = min(x, u), min(y, v)
    x2, y2 = max(x, u), max(y, v)
    for _ in range(0, 500):
        if not is_point_inside_or_boundary(randrange(x1, x2 + 1), randrange(y1, y2 + 1)):
            return False
    return True

p1 = ds[0][0]
p2 = None
for (d, ((x, y), (u, v))) in ds:
    print(".", end='', flush=True)
    if is_point_inside_or_boundary(x, v) and is_point_inside_or_boundary(u, y):
        print(d)
        if check_border(x, y, u, v):
            p2 = d
            break

print(p1, p2)
