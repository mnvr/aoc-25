import sys
from collections import defaultdict

next = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)

q = ['you']
c = 0
while len(q):
    u = q.pop()
    if u == 'out':
        c += 1
        continue
    for v in next[u]:
        q.append(v)

print(c)
