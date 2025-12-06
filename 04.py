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
    return len(changed_mx)

nx = neighbours(mx)
counts = []
while c := relax(mx, nx):
    counts.append(c)

print(counts[0], sum(counts))
