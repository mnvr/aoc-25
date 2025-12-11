import sys

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

    dist = {}
    frontier = set()

    dist[start] = 0
    frontier.add(start)

    # currently closest node to start
    def nearest():
        du, u = inf, None
        for v in frontier:
            dv = dist[v]
            if du > dv:
                (du, u) = (dv, v)
        return (du, u)

    while len(frontier):
        du, u = nearest()

        frontier.remove(u)
        if u == dest:
            return dist[u]

        # relax all neighbours
        for v in neighbours(u):
            dv = dist.get(v)
            if dv is None or dv > du + 1:
                dist[v] = du + 1
                frontier.add(v)

shortest_path_astar = shortest_path

def process(machine):
    lights, buttons, joltage = machine
    s1 = shortest_path(lights, buttons)
    # s2 = shortest_path_astar(lights, buttons)
    # s2 = shortest_path_astar(joltage, buttons)
    s2 = 0
    print(s1, s2)
    return (s1, s2)

print(*map(sum, zip(*map(process, map(parse, sys.stdin)))))
