import sys

s1, s2 = 0, 0
for line in sys.stdin:
    line = line.rstrip()

    def find(remaining):
        pos = 0
        batteries = []
        while remaining > 0:
            end = len(line) - remaining + 1
            best = max(line[pos:end])
            pos = line.index(best, pos, end) + 1
            batteries.append(best)
            remaining -= 1
        return int(''.join(batteries))

    s1 += find(2)
    s2 += find(12)

print(s1, s2)
