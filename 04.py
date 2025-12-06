import sys

mx = []
for line in sys.stdin:
    mx.append([0 if c == '.' else 1 for c in line.strip()])

def prune(mx):
    t = 0
    nx = [row[:] for row in mx]
    for y in range(0, len(mx)):
        for x in range(0, len(mx[0])):
            if not mx[y][x]:
                continue
            c = 0
            for j in range(max(0, y-1), min(y+2, len(mx))):
                for i in range(max(0, x-1), min(x+2, len(mx[0]))):
                    if not (y == j and x == i):
                        c += mx[j][i]
            if c < 4:
                t += 1
                nx[y][x] = 0
    return (t, nx)

s = []
while True:
    (t, mx) = prune(mx)
    if t == 0: break
    s.append(t)

print(s[0], sum(s))
