import sys
from collections import defaultdict, deque
from functools import cache

next = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)

@cache
def path_count(u, dest):
    if u == dest:
        return 1
    return sum((path_count(v, dest) for v in next[u]), 0)

p1 = path_count('you', 'out')

m1 = path_count('fft', 'dac')
m2 = path_count('dac', 'fft')
if m1:
    p2 = path_count('svr', 'fft') * m1 * path_count('dac', 'out')
else:
    p2 = path_count('svr', 'dac') * m2 * path_count('fft', 'out')
print(p1, p2)
