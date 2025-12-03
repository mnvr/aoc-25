def rep(n):
    match n:
        case 1: return rep1()
        case 2: return rep2()
        case 3: return rep3()
        case 4: return rep4()
        case 5: return rep5()
        case 6: return rep6()

def rep1():
    return []

def rep2():
    return [c*10 + c for c in range(1, 10)]

def rep3():
    return [c*100 + c*10 + c for c in range(1, 10)]

def rep4():
    r2 = [c*10 + d for c in range(1, 10)
                   for d in range(0, 10) if c != d] + rep(2)
    return sorted([r*100 + r for r in r2])

def rep5():
    return [c*1000 + c*100 + c*10 + c for c in range(1, 10)]

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
# print(rep6())
# print(check_range(11, 22))
print(check_range(95, 115))
print(check_range(998, 1012))
# print(check_range(1188511880, 1188511890))
print(check_range(222220, 222224))
print(check_range(446443, 446449))
