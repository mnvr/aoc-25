import sys

def check_mod(n, m):
    r = n % m
    x = n // m
    # if len(str(m)) > len(str(x)): return False
    while x > 0:
        # if len(str(x)) < len(str(m)): return False
        # print(n, m, x, r, x % m)
        if (x % m) != r:
            return False
        x = x // m
    return True

def check(n):
    m = 10
    while True: # m < n:
        if check_mod(n, m):
            return True
        m *= 10
        if m > n / 2:
            break
    return False

def check_range(a, b):
    for n in range(a, b + 1):
        if check(n):
            print(n)

def main():
    t = 0
    for seq in sys.stdin.read().split(','):
        (a, b) = [int(s) for s in seq.strip().split('-')]
        for n in range(a, b + 1):
            if check(n):
                t += n
    print(t)

main()
# check_range(11, 22)
# check_range(95, 115)
# check_range(998, 1012)
# check_range(1188511880, 1188511890)
# check_range(222220, 222224)
# print(check(11))
# print(check(101))
