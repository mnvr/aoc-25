import sys
from collections import defaultdict, deque

next = defaultdict(set)
prev = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)
        prev[v].add(u)

def path_count_pruned(start, dest):
    mid = reachable_from(start, next) & reachable_from(dest, prev)
    pruned = {}
    for u, vs in next.items():
        if u in mid:
            pruned[u] = set(filter(lambda v: v in mid, vs))
    return path_count(start, dest, pruned)

def path_count(source, dest, adj):
    q = [source]
    c = 0
    while len(q):
        u = q.pop()
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

m1, m2 = 'fft', 'dac'
if topo.index('fft') > topo.index('dac'):
    m1, m2 = 'fft', 'dac'
p1 = path_count_pruned('you', 'out')
p2 = path_count_pruned('svr', m1) * path_count_pruned(m1, m2) * path_count_pruned(m2, 'out')
print(p1, p2)
