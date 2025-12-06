import sys

ranges, ids = [], []
for line in sys.stdin:
    if line.strip():
        if '-' in line:
            (a, b) = line.split('-')
            ranges.append(range(int(a), int(b) + 1))
        else:
            ids.append(int(line))

ranges.sort(key=lambda r: (r.start, r.stop))

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

p1 = sum([id in r for id in ids for r in ranges])
p2 = sum([r.stop - r.start for r in ranges])
print(p1, p2)
