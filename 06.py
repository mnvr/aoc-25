import sys
from math import prod

lines = []
cols = None
for line in sys.stdin:
    if not line.strip(): continue
    lines.append(line)
    cs = [len(c) for c in line.split()]
    cols = map(max, zip(cs, cols if cols else cs))
cols = list(cols)

def to_num(xs):
    n = 0
    for x in xs:
        n = n * 10 + x
    return n

adds, muls = [0]*len(cols), [1]*len(cols)
result1 = 0
for line in lines:
    for (i, c) in enumerate(line.split()):
        match c:
            case '+': result1 += adds[i]
            case '*': result1 += muls[i]
            case _:
                x = int(c)
                adds[i] += x
                muls[i] *= x

result2 = 0
nums = [list([[] for _ in range(0, c)]) for c in cols]
for line in lines:
    if line[0] in ['+', '*']:
        for (i, s) in enumerate(line.split()):
            match s:
                case '+': result2 += sum(map(to_num, nums[i]))
                case '*': result2 += prod(map(to_num, nums[i]))
    else:
        a, b = 0, 0
        for c in line:
            if c != ' ' and c != '\n':
                nums[a][b].append(int(c))
            b += 1
            if b > cols[a]:
                b = 0
                a += 1

print(result1, result2)
