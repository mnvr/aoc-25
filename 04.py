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
    changed_mx = []
    changed_nx = []
    for y in range(0, len(mx)):
        for x in range(0, len(mx[0])):
            if mx[y][x] and nx[y][x] < 4:
                changed_mx.append((y, x))
                for j in range(max(0, y-1), min(y+2, len(mx))):
                    for i in range(max(0, x-1), min(x+2, len(mx[0]))):
                        changed_nx.append((j, i))
    for (y, x) in changed_mx:
        mx[y][x] -= 1
    for (y, x) in changed_nx:
        nx[y][x] -= 1
    return (mx, nx, len(changed_mx))

nx = neighbours(mx)
counts = []
while True:
    (mx, nx, c) = relax(mx, nx)
    if not c: break
    counts.append(c)

print(counts[0], sum(counts))
