import sys

mx = []
for line in sys.stdin:
    mx.append([0 if c == '.' else 1 for c in line.strip()])

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

print(t)
exit()
