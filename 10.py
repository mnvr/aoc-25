import sys
import collections

def parse(line):
    [lights, *buttons, joltage] = line.split()
    lights = tuple(1 if c == '#' else 0 for c in lights[1:-1])
    buttons = [set(int(c) for c in s[1:-1].split(',')) for s in buttons]
    joltage = tuple(int(c) for c in joltage[1:-1].split(','))
    return (lights, buttons, joltage)

def make_neighbours(buttons, action):
    def neighbours(v):
        ns = set()
        for button in buttons:
            n = list(v)
            for i in button:
                n[i] = action(n[i])
            ns.add(tuple(n))
        return ns
    return neighbours

def steps(dest, buttons, action):
    neighbours = make_neighbours(buttons, action)
    start = tuple([0] * len(dest))
    visited = set()
    queue = collections.deque([(start, 0)])

    while len(queue):
        u, d = queue.popleft()
        if u == dest:
            return d
        visited.add(u)
        for v in neighbours(u):
            if v not in visited:
                queue.append((v, d+1))

def shortest_path(dest, buttons, action):
    neighbours = make_neighbours(buttons, action)
    start = tuple([0] * len(dest))
    inf = 10000

    queue = set()
    visited = set()
    dist = collections.defaultdict(lambda: inf)
    queue.add(start)
    dist[start] = 0

    # vertex in Q with minimum dist[u]
    def min_q():
        d, u = inf, None
        for v in queue:
            if d > dist[v]:
                (d, u) = (dist[v], v)
        queue.remove(u)
        return u

    while len(queue):
        u = min_q()
        visited.add(u)
        if u == dest:
            return dist[u]
        for v in neighbours(u):
            if v not in visited:
                queue.add(v)
            alt = dist[u] + 1
            if dist[v] > alt:
                dist[v] = alt

def process(lights, buttons, joltage):
    # s1 = steps(lights, buttons, lambda v: (v + 1) % 2)
    s1 = shortest_path(lights, buttons, lambda v: (v + 1) % 2)
    # s2 = steps(joltage, buttons, lambda v: v + 1)
    return s1

p1 = list(process(*parse(line)) for line in sys.stdin)
print(sum(p1))
