import sys

def make_num(m, ns):
    for n in ns:
        m *= 10
        m += n
    return m

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

    m = max(xs[:-11])
    n = None
    ns = []
    min_ns = 10
    for x in xs:
        if n is not None:
            # print(m, len(ns), x, min_ns, ns)
            if len(ns) < 11:
                ns.append(x)
                min_ns = min(min_ns, x)
            else:
                ns0 = list(ns)
                for i in range(0, len(ns0)):
                    ns2 = list(ns)
                    del ns2[i]
                    ns2.append(x)
                    if make_num(m, ns0) < make_num(m, ns2):
                        ns0 = ns2
                ns = ns0
        if x == m:
            if n is None:
                n = 0
    p2 += make_num(m, ns)

print(p1, p2)
