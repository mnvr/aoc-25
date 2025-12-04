def rep(n):
    match n:
        case 1: return []
        case 2: return rep2()
        case 3: return rep1(n)
        case 4: return rep4()
        case 5: return rep1(n)
        case 6: return rep6()
        case 7: return rep1(n)
        case 8: return rep8()
        case 9: return rep9()
        case 10: return rep10()

def rep_even(n):
    return [] if n % 2 == 1 else rep(n)

def rep1(n):
    return [sum([c * 10**i for i in range(0, n)]) for c in range(1, 10)]

def rep2():
    return [c*10**1 + c for c in range(1, 10)]

def rep4():
    return [r*10**2 + r for r in range(10, 100)]

def rep6():
    return [r*10**4 + r*10**2 + r for r in range(10, 100)] \
           + [r*10**3 + r for r in range(100, 1000)]

def rep8():
    return [r*10**4 + r for r in range(1000, 10000)]

def rep9():
    return [r*10**6 + r*10**3 + r for r in range(100, 1000)]

def rep10():
    return [r*10**8 + r*10**6 + r*10**4 + r*10**2 + r for r in range(10, 100)] \
           + [r*10**5 + r for r in range(10000, 100000)]

def check_range(s):
    (a, b) = [int(x) for x in s.split('-')]
    rs = set(rep(len(str(a))) + rep(len(str(b))))
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
