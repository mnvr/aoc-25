import sys

def process(line):
    [out, *buttons, joltage] = line.split()
    out = [c == '#' for c in out.strip("[]")]
    buttons = [set(int(c) for c in s.strip("()").split(',')) for s in buttons]
    print(out)
    print(buttons)
    return 1

p1 = sum(process(line) for line in sys.stdin)
print(p1)
