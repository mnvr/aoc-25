import sys

mx = []
for line in sys.stdin:
    mx.append([0 if c == '.' else 1 for c in line.strip()])

def neighbours(mx):
    nx = []
    for y in range(0, len(mx)):
        nx.append([neighbour_count(mx, y, x) for x in range(0, len(mx[0]))])
    return nx

def neighbour_count(mx, y, x):
    c = -1 if mx[y][x] else 0
    for j in range(max(0, y-1), min(y+2, len(mx))):
        for i in range(max(0, x-1), min(x+2, len(mx[0]))):
            c += mx[j][i]
    return c

def pretty(mx):
    return '\n'.join([''.join(map(str, row)) for row in mx])

def pretty2(nx, ns):
    BOLD = '\033[1m'
    END = '\033[0m'
    for (y, row) in enumerate(nx):
        for (x, n) in enumerate(row):
            if (y, x) in ns:
                print(BOLD + str(n) + END, end='')
            else:
                print(n, end='')
        print()

def relax(mx, nx):
    for y in range(0, len(mx)):
        for x in range(0, len(mx[0])):
            if mx[y][x] and nx[y][x] < 4:
                print(f"- relaxing mx[{y}][{x}] with count {nx[y][x]}")
                mx[y][x] -= 1
                ns = set()
                for j in range(max(0, y-1), min(y+2, len(mx))):
                    for i in range(max(0, x-1), min(x+2, len(mx[0]))):
                        nx[j][i] -= 1
                        # print(f"  nx[{j}][{i}]")
                        if not (j == y and i == x):
                            ns.add((j, i))
                pretty2(nx, ns)
        # return (mx, nx)
    return (mx, nx)


nx = neighbours(mx)
print(pretty(nx))
(mx, nx) = relax(mx, nx)
print(pretty(nx))

exit()

def valid(mx, y, x):
    c = 0
    for j in range(max(0, y-1), min(y+2, len(mx))):
        for i in range(max(0, x-1), min(x+2, len(mx[0]))):
            c += mx[j][i]
            if c > 4:
                return False
    return c <= 4

def prune(mx):
    changed = []
    for y in range(0, len(mx)):
        for x in range(0, len(mx[0])):
            if mx[y][x] and valid(mx, y, x):
                changed.append((y, x))
    for (y, x) in changed:
        mx[y][x] = 0
    return len(changed)

s = []
while t := prune(mx):
    s.append(t)

print(s[0], sum(s))
