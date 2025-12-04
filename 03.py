import sys

s = 0
for line in sys.stdin:
    xs = [int(c) for c in line.rstrip()]
    m = max(xs[:-1])
    n = None
    for x in xs:
        if n is not None:
            n = max(n, x)
        if x == m:
            if n is None:
                n = 0
    s += m*10 + n

print(s)
