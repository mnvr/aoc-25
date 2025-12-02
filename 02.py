import sys

iv = 0
for r in sys.stdin.read().strip().split(','):
    (u, v) = [int(s) for s in r.split('-')]
    for x in range(u, v + 1):
        s = str(x)
        n = len(s)
        if n % 2 == 1:
            continue
        if s[0:n//2] == s[n//2:]:
            iv += x
print(iv)
