import sys

def num(m, ns):
    for n in ns:
        m *= 10
        m += n
    return m


p1, p2 = 0, 0
s1, s2 = 0, 0
for line in sys.stdin:
    xs = [int(c) for c in line.rstrip()]

    pos = 0
    remaining = 2
    batteries = []
    while remaining > 0:
        best = max(xs[pos:len(xs)-remaining+1])
        i = xs.index(best, pos, len(xs)-remaining+1)
        pos = i
        batteries.append(best)
        remaining -= 1
    z = ''.join(map(str, batteries))
    print(z)

    m = max(xs[:-1])
    p1 += m*10 + max(xs[xs.index(m)+1:])

    m = max(xs[:-11])
    mi = xs.index(m)
    ns = xs[mi+1:mi+12]
    for x in xs[mi+12:]:
        n = num(m, ns)
        for i in range(0, 11):
            ns2 = ns[:i] + ns[i+1:] + [x]
            if n < num(m, ns2):
                ns = ns2
                break
    p2 += num(m, ns)

print(p1, p2)
