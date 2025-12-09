import sys
from itertools import combinations
from collections import defaultdict

tiles = [list(map(int, line.split(','))) for line in sys.stdin]

def dist(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

ds = (dist(a, b) for (a, b) in combinations(tiles, 2))

p1 = max(ds)
print(p1)

vertical_lines = defaultdict(list)
horizontal_lines = defaultdict(list)
max_x = 0
max_y = 0
for start, end in zip(tiles, tiles[1:] + [tiles[0]]):
    (a, b) = start
    (u, v) = end
    max_x = max(max_x, a, u)
    max_y = max(max_y, b, v)
    if a == u:
        vertical_lines[a].append((min(b, v), max(b, v)))
    else:
        horizontal_lines[b].append((min(a, u), max(a, u)))
# horizontal_lines = dict(horizontal_lines)
# vertical_lines = dict(vertical_lines)

print(max_x, max_y)
print(horizontal_lines)
print(vertical_lines)

def print1(s):
    # print(s)
    pass

def is_point_on_boundary(x, y):
    # On boundary
    for a, b in horizontal_lines[y]:
        if a <= x and x <= b:
            return True
    for a, b in vertical_lines[x]:
        if a <= y and y <= b:
            return True

def is_point_inside(x, y):
    res = _is_point_inside(x, y)
    print1(f"is_point_inside({x}, {y}): {res}")
    return res

def _is_point_inside(x, y):
    # # On boundary
    # for a, b in horizontal_lines[y]:
    #     if a <= x and x <= b:
    #         return True
    # for a, b in vertical_lines[x]:
    #     if a <= y and y <= b:
    #         return True

    # Inside interior
    inside = False
    xr = range(0, x) #if x < (max_x - x) else range(x, max_x)
    for u in xr:
        if any(a < y and y < b for a, b in vertical_lines[u]):
            # print(f"testing point ({x}, {y}) u {u} found vertical crossing and will flip inside to {not inside}")
            inside = not inside
    if not inside:
        return False
    return True
    yr = range(0, y) #if y < (max_y - y) else range(y, max_y)
    for v in yr:
        if is_point_on_boundary(x, v):
            continue
        if any(a < x and x < b for a, b in horizontal_lines[v]):
            inside = not inside
    return inside

print("012345678901234")
for y in range(0, max_y + 3):
    if y < 10:
        print(f"{y}", end='')
    else:
        print(" ", end='')
    for x in range(0, max_x + 3):
        if is_point_on_boundary(x, y):
            print('#', end='')
        elif is_point_inside(x, y):
            print('\033[37m#\033[0m', end='')
        else:
            print('.', end='')
        # print('#' if is_point_inside(x, y) else '.', end='')
    print()
