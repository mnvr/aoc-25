import sys
from collections import Counter

splits, paths = 0, Counter()
for line in sys.stdin:
    for (i, c) in enumerate(line.strip()):
        match c:
            case 'S':
                paths[i] = 1
            case '^':
                if i in paths:
                    splits += 1
                    paths[i-1] += paths[i]
                    paths[i+1] += paths[i]
                    del paths[i]

print(splits, paths.total())
