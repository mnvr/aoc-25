import sys

def num(m, ns):
    for n in ns:
        m *= 10
        m += n
    return m

p1, p2 = 0, 0
for line in sys.stdin:
    xs = [int(c) for c in line.rstrip()]

    m = max(xs[:-1])
    n = 0
    for x in xs[xs.index(m)+1:]:
        n = max(n, x)
    p1 += m*10 + n

    m = max(xs[:-11])
    mi = xs.index(m)
    ns = xs[mi+1:mi+12]
    for x in xs[mi+12:]:
        for i in range(0, 11):
            ns2 = ns[:i] + ns[i+1:] + [x]
            if num(m, ns) < num(m, ns2):
                ns = ns2
                break
    p2 += num(m, ns)

print(p1, p2)
