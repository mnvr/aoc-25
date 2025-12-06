import sys

ranges, ids = [], []
for line in sys.stdin:
    if line.strip():
        if '-' in line:
            (a, b) = line.split('-')
            ranges.append(range(int(a), int(b) + 1))
        else:
            ids.append(int(line))

def sorted_ranges(r):
    return list(map(lambda t: range(t[0], t[1]), sorted(map(lambda r: (r.start, r.stop), ranges))))

ranges = sorted_ranges(ranges)
i = 0
while i < len(ranges):
    r1 = ranges[i]
    j = i + 1
    while j < len(ranges):
        r2 = ranges[j]
        if r2.start <= r1.stop:
            r1 = range(r1.start, max(r1.stop, r2.stop))
            ranges[i] = r1
            del ranges[j]
        else:
            break
    i += 1

p1 = sum([1 for id in ids for r in ranges if id in r])
p2 = sum([r.stop - r.start for r in ranges])
print(p1, p2)
