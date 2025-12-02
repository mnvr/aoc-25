import sys

iv, iv2 = 0, 0
for r in sys.stdin.read().strip().split(','):
    (u, v) = [int(s) for s in r.split('-')]
    for x in range(u, v + 1):
        s = str(x)
        n = len(s)
        for i in range(n//2, 0, -1):
            a = s[0:i]
            j = i
            while j < n:
                b = s[j:i+j]
                if a != b:
                    break
                j += i
            if j == n:
                if i + i == n:
                    iv += x
                iv2 += x
                break

print(iv, iv2)
