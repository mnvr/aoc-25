def rep(n):
    match n:
        case 2: return rep2()
        case 3: return rep1(n)
        case 4: return rep4()
        case 5: return rep1(n)
        case 6: return rep6()
        case 7: return rep1(n)
        case 8: return rep8()
        case 9: return rep9()
        case 10: return rep10()

def rep1(n):
    return [sum([c * 10**i for i in range(0, n)]) for c in range(1, 10)]

def rep2():
    return [c*10**1 + c for c in range(1, 10)]

def rep4():
    return [r*10**2 + r for r in range(10, 100)]

def rep6():
    return [r*10**4 + r*10**2 + r for r in range(10, 100)] + [r*10**3 + r for r in range(100, 1000)]

def rep8():
    return [r*10**4 + r for r in range(1000, 10000)]

def rep9():
    return [r*10**6 + r*10**3 + r for r in range(100, 1000)]

def rep10():
    return [r*10**8 + r*10**6 + r*10**4 + r*10**2 + r for r in range(10, 100)] + [r*10**5 + r for r in range(10000, 100000)]

def check_range(a, b):
    rs = set(rep(len(str(a))) + rep(len(str(b))))
    span = range(a, b + 1)
    for r in rs:
        if r in span:
            yield r

def to_range(s):
    return [int(x) for x in s.split('-')]

import sys
print(sum([x for s in sys.stdin.read().strip().split(',') for x in check_range(*to_range(s))]))
# sum([x for x in check_range(*to_range(s)) for s in sys.stdin.read().strip().split(',')])

# check_range(11, 22)
# check_range(95, 115)
# check_range(998, 1012)
# check_range(222220, 222224)
# check_range(446443, 446449)
# check_range(38593856, 38593862)
# check_range(1188511880, 1188511890)
# # print(sorted(rep(10)))
