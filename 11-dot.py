import sys
from collections import defaultdict

next = defaultdict(set)
for line in sys.stdin:
    u, vs = line.split(':')
    for v in vs.split():
        next[u].add(v)

print("digraph {")
print("\t{")
print("\t\tnode [style=filled, fillcolor=beige]")
print("\t\tsvr -> fft [style=invis]")
print("\t\tfft -> dac [style=invis]")
print("\t\tdac -> out [style=invis]")
print("\t}")
for u, vs in next.items():
    for v in vs:
        print(f"\t{u} -> {v}")
print("}")
