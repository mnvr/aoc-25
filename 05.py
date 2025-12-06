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

def sorted_ranges(r):
    return list(map(lambda t: range(t[0], t[1]), sorted(map(lambda r: (r.start, r.stop), ranges))))

ranges = sorted_ranges(ranges)
print(ranges)

i = 0
while i < len(ranges):
    r1 = ranges[i]
    print(f"Inspecting range {r1}")
    j = i + 1
    while j < len(ranges):
        r2 = ranges[j]
        if r2.start <= r1.stop:
            r1 = range(r1.start, r2.stop)
            ranges[i] = r1
            del ranges[j]
        else:
            j += 1
    i += 1
print(ranges)

print(sum([r.stop - r.start for r in ranges]))
exit()

def merge(ri, rj):
    u, v = ri.start, ri.stop
    x, y = rj.start, rj.stop
    if v < x or y < u:
        return None
    else:
        u = min(u, x)
        v = max(v, y)
        return range(u, v)

def key(r):
    return (r.start, r.stop)

merged = None
p2 = 0
for _ in range(0, 150):
    if merged is None:
        merged = {}
    else:
        ranges = list(merged.values())
    # print(ranges)
    for (i, ri) in enumerate(ranges):
        for (j, rj) in enumerate(ranges):
            if i == j: continue
            ki, kj = key(ri), key(rj)
            # print(f"Considering {ki}, {kj}:", end=' ')
            rm = merge(ri, rj)
            if rm is None:
                merged[key(ri)] = ri
                # print(f"no overlap, adding {ki}")
            else:
                km = key(rm)
                # print(f"overlap, adding {km}")
                # print(merged, key(ri))
                if key(ri) in merged:
                    del merged[key(ri)]
                    # print(f"Removed {ki}")
                if key(rj) in merged:
                    del merged[key(rj)]
                    # print(f"Removed {kj}")
                merged[key(rm)] = rm
    prev_p2 = p2
    p2 = sum([r.stop - r.start for r in ranges])

print(fc, p2)
