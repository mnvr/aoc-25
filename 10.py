import sys

def parse(line):
    [lights, *buttons, joltage] = line.split()
    lights = [c == '#' for c in lights.strip("[]")]
    buttons = [set(int(c) for c in s.strip("()").split(',')) for s in buttons]
    return (lights, buttons)

def process(lights, buttons):
    print(lights)
    print(buttons)
    return 1

p1 = sum(process(*parse(line)) for line in sys.stdin)
print(p1)
