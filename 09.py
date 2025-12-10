import sys
from itertools import combinations
from collections import defaultdict

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

def is_point_on_boundary(x, y):
    for a, b in horizontal_lines[y]:
        if a <= x and x <= b:
            return True
    for a, b in vertical_lines[x]:
        if a <= y and y <= b:
            return True
    return False

def is_point_inside_or_boundary(x, y):
    if is_point_on_boundary(x, y):
        return True

    for u in range(0, x):
        if is_point_on_boundary(u, y):
            break
    else:
        return False

    for u in range(x+1, max_x+1):
        if is_point_on_boundary(u, y):
            break
    else:
        return False

    for v in range(0, y):
        if is_point_on_boundary(x, v):
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

p1 = ds[0][0]
p2 = None
for (d, ((x, y), (u, v))) in ds:
    if is_point_inside_or_boundary(x, v) and is_point_inside_or_boundary(u, y):
        p2 = d
        break

print(p1, p2)
