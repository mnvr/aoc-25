def rep(n):
    if n % 2 == 1: return rep_odd(n)
    match n:
        case 2: return rep2()
        case 4: return rep4()
        case 6: return rep6()

def rep_odd(n):
    return [sum([c * 10**i for i in range(0, n)]) for c in range(1, 10)]

def rep2():
    return [c*10 + c for c in range(1, 10)]

def rep4():
    r2 = [c*10 + d for c in range(1, 10)
                   for d in range(0, 10) if c != d] + rep(2)
    return sorted([r*100 + r for r in r2])

def rep6():
    r2 = [c*10 + d for c in range(1, 10)
                   for d in range(0, 10)]
    r3 = [c*100 + d*10 + e for c in range(1, 10)
                           for d in range(0, 10)
                           for e in range(0, 10)]
    r6 = [r*10000 + r*100 + r for r in r2] + [r*1000 + r for r in r3]
    return sorted(set(r6))

def check_range(a, b):
    rs = set(rep(len(str(a))) + rep(len(str(b))))
    span = range(a, b + 1)
    for r in rs:
        if r in span:
            print(r)

# print([v for n in range(1, 5) for v in rep(n)])
# print(check_range(11, 22))
# print(check_range(95, 115))
print(check_range(998, 1012))
# # print(check_range(1188511880, 1188511890))
print(check_range(222220, 222224))
# print(check_range(446443, 446449))
