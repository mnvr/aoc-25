import sys
from collections import defaultdict, deque

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

def path_count_bfs(source, dest, adj):
    q = deque([source])
    c = 0
    i = 0
    while len(q):
        if i % 10000 == 1:
            print('.', end='', flush=True)
        i += 1
        u = q.popleft()
        if u == dest:
            c += 1
            continue
        for v in adj[u]:
            q.append(v)
    return c

def topological_sort(start, adj):
    topo = []
    visited = set()
    def build_topo(u):
        if not u in visited:
            visited.add(u)
            for v in adj[u]:
                build_topo(v)
            topo.append(u)
    build_topo(start)
    return reversed(topo)

def reachable_from(start, adj):
    visited = set()
    def step(u):
        if not u in visited:
            visited.add(u)
            for v in adj[u]:
                step(v)
    step(start)
    return visited

topo = list(topological_sort('svr', next))
print(len(topo))
si = topo.index('svr')
fi = topo.index('fft')
di = topo.index('dac')
oi = topo.index('out')
print([si, fi, di, oi])
from_fft = reachable_from('fft', next)
to_dest = reachable_from('dac', prev)
mid = from_fft & to_dest
print(len(from_fft), len(to_dest), len(mid))
# exit()
# mid = set(filter(lambda v: v in from_fft, topo[fi:di+1]))
pruned = {}
for u, vs in next.items():
    if u in mid:
        pruned[u] = set(filter(lambda v: v in mid, vs))
print("pruned length", len(pruned))
# print(path_count_bfs('dac', 'fft', prev))
z = path_count_bfs('fft', 'dac', pruned)
print(z)
# print(path_count_bfs('fft', 'dac', pruned))
z1 = path_count_bfs('fft', 'svr', prev)
print(z1)
z2 = path_count_bfs('dac', 'out', next)
print(z2)
print(z * z1 * z2)
# print(path_count_bfs('dac', 'fft', prev))
# print(path_count_bfs('fft', 'dac', next))
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
