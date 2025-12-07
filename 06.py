import sys
from math import prod

nlen = None
lines = []
for line in sys.stdin:
    lines.append(line)
    nl = [len(c) for c in line.split()]
    nlen = map(max, zip(nl, nlen if nlen else nl))
nlen = list(nlen)

def to_num(xs):
    n = 0
    for x in xs:
        n = n * 10 + x
    return n

result = 0
nums = [list([[] for _ in range(0, l)]) for l in nlen]
# print(nums)
for line in lines:
    if line[0] in ['+', '*']:
        for (i, s) in enumerate(line.split()):
            # print(nums[i])
            match s:
                case '+': result += sum(map(to_num, nums[i]))
                case '*': result += prod(map(to_num, nums[i]))
    else:
        a, b = 0, 0
        for c in line:
            if c != ' ' and c != '\n':
                nums[a][b].append(int(c))
            b += 1
            if b > nlen[a]:
                b = 0
                a += 1

    # print(nums)

print(result)
exit()

adds, muls = [0]*1000, [1]*1000
result = 0
for line in sys.stdin:
    for (i, c) in enumerate(line.split()):
        match c:
            case '+': result += adds[i]
            case '*': result += muls[i]
            case _:
                x = int(c)
                adds[i] += x
                muls[i] *= x

print(result)
