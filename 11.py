import sys
from collections import defaultdict

next = defaultdict(set)
prev = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)
        prev[v].add(u)

def path_count(source, dest, adj):
    q = [source]
    c = 0
    i = 0
    while len(q):
        if i % 10000 == 1:
            print('.', end='', flush=True)
        i += 1
        u = q.pop()
        if u == dest:
            c += 1
            continue
        for v in adj[u]:
            q.append(v)
    return c

print(path_count('fft', 'svr', prev))
# print(path_count('fft', 'dac'))
print(path_count('dac', 'out', next)) # <-
exit()

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

q = [('svr', 0, 'svr')]
c = 0
while len(q):
    u, history, path = q.pop()
    if u == 'out':
        print(path)
        if history == 3:
            c += 1
        continue
    if u == 'dac':
        history |= 2
    if u == 'fft':
        history |= 1
    for v in next[u]:
        q.append((v, history, path + ',' + (f'\033[1m{v}\033[0m' if v in ['dac', 'fft'] else v)))

print(c)
