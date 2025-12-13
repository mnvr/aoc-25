import sys
from collections import defaultdict

next = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)


def path_count(source, dest):
    q = [source]
    c = 0
    while len(q):
        u = q.pop()
        if u == dest:
            c += 1
            continue
        for v in next[u]:
            q.append(v)
    return c

print(path_count('svr', 'fft'))
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
