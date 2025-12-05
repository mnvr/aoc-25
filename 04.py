import sys

mx = []
for line in sys.stdin:
    mx.append([0 if c == '.' else 1 for c in line.strip()])

def prune(mx):
    nx = list(map(lambda row: list(row), mx))
    t = 0
    for y in range(0, len(mx)):
        for x in range(0, len(mx[0])):
            if mx[y][x] != 1:
                continue
            s = 0
            for j in range(max(0, y-1), min(y+2, len(mx))):
                for i in range(max(0, x-1), min(x+2, len(mx[0]))):
                    if not (y == j and x == i):
                        s += (mx[j][i])
            if s < 4:
                t += 1
                nx[y][x] = 0
    return (t, nx)

t0 = 0
(t, mx) = prune(mx)
p1 = t
t0 += t
while t != 0:
    (t, mx) = prune(mx)
    t0 += t

print(p1, t0)
