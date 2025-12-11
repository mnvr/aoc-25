import sys
import collections

def parse(line):
    [lights, *buttons, joltage] = line.split()
    lights = tuple(1 if c == '#' else 0 for c in lights[1:-1])
    buttons = [set(int(c) for c in s[1:-1].split(',')) for s in buttons]
    joltage = tuple(int(c) for c in joltage[1:-1].split(','))
    return (lights, buttons, joltage)

def shortest_path(dest, buttons):
    def neighbours(v):
        ns = set()
        for button in buttons:
            n = list(v)
            for i in button:
                n[i] = (n[i] + 1) % 2
            ns.add(tuple(n))
        return ns

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
            if v in visited:
                continue
            queue.add(v)
            alt = dist[u] + 1
            if dist[v] > alt:
                dist[v] = alt

def shortest_path_astar(dest, buttons):
    def neighbours(v):
        ns = set()
        for button in buttons:
            n = list(v)
            for i in button:
                n[i] = (n[i] + 1)
            ns.add(tuple(n))
        return ns

    start = tuple([0] * len(dest))
    inf = 10000

    queue = set()
    visited = set()
    dist = collections.defaultdict(lambda: inf)
    queue.add(start)
    dist[start] = 0

    # vertex in Q with minimum dist[u] and some heuristic
    def min_q_star():
        d, h, u = inf, 0, None
        def heuristic(v):
            return len(v)
        for v in queue:
            dv = dist[v]
            if d > dv:
                (d, h, u) = (dv, heuristic(v), v)
            elif d == dv and heuristic(v) > h:
                (d, h, u) = (dv, heuristic(v), v)
        queue.remove(u)
        return u

    while len(queue):
        u = min_q_star()
        # print(len(queue), u, dest)
        visited.add(u)
        if u == dest:
            return dist[u]
        for v in neighbours(u):
            if any(a > b for a, b in zip(v, dest)):
                continue
            if v not in visited:
                queue.add(v)
            alt = dist[u] + 1
            if dist[v] > alt:
                dist[v] = alt

def process(machine):
    lights, buttons, joltage = machine
    s1 = shortest_path(lights, buttons)
    s2 = shortest_path_astar(joltage, buttons)
    print(s1, s2)
    return (s1, s2)

print(*map(sum, zip(*map(process, map(parse, sys.stdin)))))
