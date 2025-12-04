import sys

p1, p2 = 0, 0
for line in sys.stdin:
    xs = [int(c) for c in line.rstrip()]
    m = max(xs[:-1])
    n = None
    ns = []
    min_ns = 10
    for x in xs:
        if n is not None:
            n = max(n, x)
        if x == m:
            if n is None:
                n = 0
    p1 += m*10 + n

    m = max(xs[:-12])
    n = None
    ns = []
    min_ns = 10
    for x in xs:
        if n is not None:
            print(m, len(ns), x, min_ns, ns)
            if len(ns) < 11:
                ns.append(x)
                min_ns = min(min_ns, x)
            elif x >= min_ns:
                for (i, y) in enumerate(ns):
                    if y == min_ns:
                        print("deleting", ns[i])
                        del ns[i]
                        ns.append(x)
                        min_ns = min(ns)
                        break
        if x == m:
            if n is None:
                n = 0
    z = m
    for y in ns:
        z *= 10
        z += y
    p2 += z

print(p1, p2)
