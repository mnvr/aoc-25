import sys

pos, z1, z2 = 50, 0, 0
for s in sys.stdin:
    if s[0] == 'L':
        pos = (100 - pos) % 100
    pos += int(s[1:])
    z2 += pos // 100
    pos %= 100
    z1 += 1 if pos == 0 else 0
    if s[0] == 'L':
        pos = (100 - pos) % 100

print(z1, z2)
