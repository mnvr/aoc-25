import sys

pos = 50
z = 0
rotations = [(s[0], int(s[1:])) for s in sys.stdin]
for (d, steps) in rotations:
    print(d, steps, pos, z)
    pos = (pos + (-1 if d == 'L' else 1) * steps) % 100
    z = z + (1 if pos == 0 else 0)

print(pos, z)
