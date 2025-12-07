import sys
from math import prod

op = None
r = 0
nums = []
for row in zip(*sys.stdin.read().strip().split('\n')):
    row = ''.join(row).strip()
    if not row:
        if op == '+':
            r += sum(nums)
        elif op == '*':
            r += prod(nums)
        else:
            raise "wtf"
        op = None
        nums = []
    else:
        if op is None:
            op = row[-1]
            row = row[:-1]
        nums.append(int(row))

print(r)
# print(list(zip(*sys.stdin.read().split('\n'))))
exit()
lines = []
cols = None
for line in sys.stdin:
    if not line.strip(): continue
    lines.append(line)
    cs = [len(c) for c in line.split()]
    cols = map(max, zip(cs, cols if cols else cs))
cols = list(cols)

p1 = 0
adds, muls = [0]*len(cols), [1]*len(cols)
for line in lines:
    for (i, c) in enumerate(line.split()):
        match c:
            case '+': p1 += adds[i]
            case '*': p1 += muls[i]
            case _:
                x = int(c)
                adds[i] += x
                muls[i] *= x

p2 = 0
nums = [[0]*c for c in cols]
for line in lines:
    if line[0] in ['+', '*']:
        for (i, s) in enumerate(line.split()):
            match s:
                case '+': p2 += sum(nums[i])
                case '*': p2 += prod(nums[i])
    else:
        a, b = 0, 0
        for c in line:
            if c != ' ' and c != '\n':
                nums[a][b] = nums[a][b] * 10 + int(c)
            b += 1
            if b > cols[a]:
                b = 0
                a += 1

print(p1, p2)
