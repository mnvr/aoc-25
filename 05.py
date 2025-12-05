import sys

ranges = []
fc = None
for line in sys.stdin:
    if fc is None:
        if '-' in line:
            (a, b) = line.split('-')
            ranges.append(range(int(a), int(b) + 1))
        else:
            fc = 0
    else:
        id = int(line)
        for r in ranges:
            if id in r:
                fc += 1
                break

print(fc)
