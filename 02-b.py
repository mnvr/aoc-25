def check_mod(n, m):
    r = n % m
    x = n // m
    while x > 0:
        # print(n, m, x, r, x % m)
        if (x % m) != r:
            return False
        x = x // m
    return True

def check(n):
    m = 10
    while m <= n / 2:
        if check_mod(n, m):
            return True
        m *= 10
    return False


def check_range(a, b):
    for n in range(a, b + 1):
        if check(n):
            print(n)

print(check_range(11, 22))
print(check_range(95, 115))
print(check_range(998, 1012))
print(check_range(1188511880, 1188511890))
# print(check(101))
