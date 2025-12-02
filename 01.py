import sys

pos, z1, z2 = 50, 0, 0
for steps in [(-1 if s[0] == 'L' else 1) * int(s[1:]) for s in sys.stdin]:
    (m, p) = divmod(pos + steps, 100)
    if m < 0 and pos == 0:
        m += 1
    if m > 0 and p == 0:
        m -= 1
    z1 += 1 if p == 0 else 0
    z2 += abs(m)
    pos = p

print(z1, z1 + z2)
