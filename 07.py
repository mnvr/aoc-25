import sys
from collections import Counter

xs = set()
paths = Counter()
xm = 0
p1 = 0
for line in sys.stdin:
    for (i, c) in enumerate(line.strip()):
        xm = max(xm, i)
        match c:
            case 'S':
                xs.add(i)
                paths[i] = 1
            case '^':
                if i in xs:
                    p1 += 1
                    paths[i-1] += paths[i]
                    paths[i+1] += paths[i]
                    del paths[i]
                    # print(f"removing {i} adding {i - 1} and {i + 1}")
                    xs.remove(i)
                    xs.add(i - 1)
                    xs.add(i + 1)
    # print(sorted(xs))

xs = filter(lambda x: x >= 0 and x <= xm, xs)
# print(len(list(xs)))
print(p1)
print(paths.total())
