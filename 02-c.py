def rep(n):
    if n % 2 == 1: return rep_odd(n)
    match n:
        case 2: return rep2()
        case 4: return rep4()
        case 6: return rep6()
        case 8: return rep8()
        case 10: return rep10()

def rep_odd(n):
    return [sum([c * 10**i for i in range(0, n)]) for c in range(1, 10)]

def rep2():
    return [c*10**1 + c for c in range(1, 10)]

def rep4():
    return [r*10**2 + r for r in range(1, 10**2)]

def rep6():
    return [r*10**4 + r*10**2 + r for r in range(1, 10**2)] + [r*10**3 + r for r in range(1, 10**3)]

def rep8():
    return [r*10**4 + r for r in range(1, 10**4)] + [r*10**4 + r for r in rep4()]

# def rep10():
#     return [r*10**8 + r*10**6 + r*10**4 + r**10*2 + r for r in _r2()] + \
#            [r*10**5 + r for r in rep(5)]

def check_range(a, b):
    rs = set(rep(len(str(a))) + rep(len(str(b))))
    span = range(a, b + 1)
    for r in rs:
        if r in span:
            print(r)

check_range(11, 22)
check_range(95, 115)
check_range(998, 1012)
check_range(222220, 222224)
check_range(446443, 446449)
check_range(38593856, 38593862)
# check_range(1188511880, 1188511890)
