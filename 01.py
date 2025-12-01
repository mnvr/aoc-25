import sys
import math

pos = 50
z1 = 0
z2 = 0
rotations = [(s[0], int(s[1:])) for s in sys.stdin]
print(' ', 0, pos, z1, z2)
for (d, steps) in rotations:
    (m, p) = divmod(pos + ((-1 if d == 'L' else 1) * steps), 100)
    if m < 0 and pos == 0:
        m += 1
    if m > 0 and p == 0:
        m -= 1
    z1 = z1 + (1 if p == 0 else 0)
    z2 = z2 + (1 if p == 0 else 0) + abs(m)
    pos = p
    print(d, steps, pos, z1, z2, m)

print(pos, z1, z2)
