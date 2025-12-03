def rep(n):
    match n:
        case 1: return rep1()
        case 2: return rep2()
        case 3: return rep3()
        case 4: return rep1()
        case 5: return rep1()

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
                   for d in range(0, 10) if c != d] + rep(2)
    r3 = [c*100 + d*10 + e for c in range(1, 10)
                           for d in range(0, 10)
                           for e in range(0, 10) if c != d] + rep(3)
    return sorted([r*10000 + r*100 + r for r in r2])

# print([v for n in range(1, 5) for v in rep(n)])
print(rep6())
