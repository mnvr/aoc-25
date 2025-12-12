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

q = [('svr', 0)]
c = 0
while len(q):
    u, history = q.pop()
    if u == 'out':
        if history == 3:
            c += 1
        continue
    if u == 'dac':
        history |= 2
    if u == 'fft':
        history |= 1
    for v in next[u]:
        q.append((v, history))

print(c)
