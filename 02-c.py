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

print([v for n in range(1, 4) for v in rep(n)])
