import sys
from heapq import heappush, heappop

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

    dist = {}
    frontier = []

    dist[start] = 0
    heappush(frontier, (0, start))

    while len(frontier):
        du, u = heappop(frontier)

        if u == dest:
            return du

        # relax all neighbours
        for v in neighbours(u):
            dv = dist.get(v)
            if dv is None or dv > du + 1:
                dv = du + 1
                dist[v] = dv
                heappush(frontier, (dv, v))

def shortest_path_astar(dest, buttons):
    dn = list(dest)

    def neighbours(v):
        ns = set()
        for button in buttons:
            n = list(v)
            for i in button:
                n[i] = n[i] + 1
            if any(n[i] > dn[i] for i in range(len(dn))):
                continue
            ns.add(tuple(n))
        return ns

    def potential(v):
        z = sum(a - b for a, b in zip(dest, v))
        assert z >= 0
        return z

    start = tuple([0] * len(dest))

    dist = {}
    frontier = []

    dist[start] = 0
    heappush(frontier, (0 + potential(start), 0, start))

    while len(frontier):
        _, du, u = heappop(frontier)
        if u == dest:
            return du

        # relax all neighbours
        for v in neighbours(u):
            dv = dist.get(v)
            if dv is None or dv > du + 1:
                dv = du + 1
                dist[v] = dv
                heappush(frontier, (dv + potential(v), dv, v))

def bin_pack(dest, buttons):
    dest = list(dest)
    start = [0] * len(dest)
    buttons = [list(1 if i in button else 0 for i in range(len(dest))) for button in buttons]
    buttons = sorted(buttons, key=len, reverse=True)
    start, dest = dest, start
    print(start, dest, buttons)
    return 0

def process(machine):
    lights, buttons, joltage = machine
    s1 = 0
    # s1 = shortest_path(lights, buttons)
    s2 = bin_pack(joltage, buttons)
    print(s1, s2)
    return (s1, s2)

print(*map(sum, zip(*map(process, map(parse, sys.stdin)))))
