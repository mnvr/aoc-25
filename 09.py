import sys
from itertools import combinations
from collections import defaultdict

tiles = [list(map(int, line.split(','))) for line in sys.stdin]

def dist(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

# ds = (dist(a, b) for (a, b) in combinations(tiles, 2))
ds = ((dist(a, b), (a, b)) for (a, b) in combinations(tiles, 2))
ds = list(sorted(ds, reverse=True))

# p1 = max(ds)
p1 = ds[0][0]
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

# print(max_x, max_y)
# print(horizontal_lines)
# print(vertical_lines)

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

def vis(s):
    print("012345678901234")
    for y in range(0, max_y + 3):
        if y < 10:
            print(f"{y}", end='')
        else:
            print(" ", end='')
        for x in range(0, max_x + 3):
            if (x, y) in s:
                print('*', end='')
            elif is_point_on_boundary(x, y):
                print('#', end='')
            else:
                print('.', end='')
            # else:
            #     print('\033[37m#\033[0m', end='')
            # print('#' if is_point_inside(x, y) else '.', end='')
        print()
    print()

def is_wall(x, y):
    return any(a <= y and y <= b for a, b in vertical_lines[x]) or \
        any(a <= x and x <= b for a, b in horizontal_lines[y])

def neighbours(x, y):
    ds = [-1, 0, +1]
    return [(x+u, y+v) for u in ds for v in ds if (u != 0 or v != 0) and (x+u) >= 0 and (x+u) <= max_x and (y+v) >= 0 and (y+v) <= max_y]

def floodfill_out():
    v = set()
    q = [(0, 0)]
    print(max_x, max_y, max_x * max_y)
    while len(q):
        (x, y) = q.pop()
        # vis(v)
        for n in neighbours(x, y):
            if n not in v and not is_wall(n[0], n[1]):
                v.add(n)
                q.append(n)
    return v

def floodfill_in():
    v = set()
    # q = [ds[0][1][1]]
    (z1, z2) = ds[0][1][1]
    q = [(z1+1, z2+1)]
    print(max_x, max_y, max_x * max_y)
    while len(q):
        (x, y) = q.pop()
        # vis(v)
        for n in neighbours(x, y):
            if n not in v and not is_wall(n[0], n[1]):
                v.add(n)
                q.append(n)
    return v

def is_point_inside_or_boundary(x, y):
    res = _is_point_inside_or_boundary(x, y)
    print1(f"is_point_inside_or_boundary({x}, {y}): {res}")
    return res

def _is_point_inside_or_boundary(x, y):
    if is_point_on_boundary(x, y):
        return True

    for u in range(0, x):
        # print("1", u, y, is_point_on_boundary(u, y))
        if is_point_on_boundary(u, y):
            break
    else:
        return False

    for x in range(x+1, max_x+1):
        # print("2", u, y, is_point_on_boundary(u, y))
        if is_point_on_boundary(u, y):
            break
    else:
        return False

    for v in range(0, y):
        # print("3", x, v, is_point_on_boundary(x, v))
        if is_point_on_boundary(x, v):
            break
    else:
        return False

    for v in range(y+1, max_y+1):
        # print("3", x, v, is_point_on_boundary(x, v))
        if is_point_on_boundary(x, v):
            break
    else:
        return False

    return True

# print(is_point_inside_or_boundary(10, 4))
# exit()
print("012345678901234")
for y in range(0, max_y + 3):
    if y < 10:
        print(f"{y}", end='')
    else:
        print(" ", end='')
    for x in range(0, max_x + 3):
        if is_point_on_boundary(x, y):
            print('#', end='')
        elif is_point_inside_or_boundary(x, y):
            print('\033[37m#\033[0m', end='')
        else:
            print('.', end='')
        # print('#' if is_point_inside(x, y) else '.', end='')
    print()
