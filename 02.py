def rep1(n):
    return [sum([c * 10**i for i in range(0, n)]) for c in range(1, 10)]

rep = {
    1: set([]),
    2: set([c*10**1 + c for c in range(1, 10)]),
    3: set(rep1(3)),
    4: set([r*10**2 + r for r in range(10, 100)]),
    5: set(rep1(5)),
    6: set([r*10**4 + r*10**2 + r for r in range(10, 100)] \
           + [r*10**3 + r for r in range(100, 1000)]),
    7: set(rep1(7)),
    8: set([r*10**4 + r for r in range(1000, 10000)]),
    9: set([r*10**6 + r*10**3 + r for r in range(100, 1000)]),
    10: set([r*10**8 + r*10**6 + r*10**4 + r*10**2 + r for r in range(10, 100)] \
           + [r*10**5 + r for r in range(10000, 100000)])
}

def check_range(s):
    (a, b) = [int(x) for x in s.split('-')]
    rs = rep[len(str(a))].union(rep[len(str(b))])
    all = [r for r in rs if r in range(a, b + 1)]
    even = [r for r in all if r//(h := 10**(len(str(r))//2)) == r%h]
    return (even, all)

import sys

p1, p2 = 0, 0
for r in sys.stdin.read().strip().split(','):
    (even, all) = check_range(r)
    p1 += sum(even)
    p2 += sum(all)

print(p1, p2)
