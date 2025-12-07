import sys
from math import prod

lines = list(filter(bool, sys.stdin.read().split('\n')))

r1 = 0
for group in zip(*[row.split() for row in lines]):
    nums = map(int, group[:-1])
    r1 += sum(nums) if group[-1] == '+' else prod(nums)

op = None
r2 = 0
nums = []
for row in zip(*lines):
    row = ''.join(row).strip()
    if not row:
        r2 += sum(nums) if op == '+' else prod(nums)
        op = None
        nums = []
    else:
        if op is None:
            op = row[-1]
            row = row[:-1]
        nums.append(int(row))

r2 += sum(nums) if op == '+' else prod(nums)

print(r1, r2)
