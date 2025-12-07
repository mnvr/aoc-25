import sys
from math import prod

lines = list(filter(bool, sys.stdin.read().split('\n')))

r1 = 0
for (*nums, op) in zip(*(map(str.split, lines))):
    nums = map(int, nums)
    r1 += sum(nums) if op == '+' else prod(nums)

r2 = 0
op, nums = None, []
for row in zip(*lines):
    row = ''.join(row).strip()
    if not row:
        r2 += sum(nums) if op == '+' else prod(nums)
        op, nums = None, []
    else:
        if op is None:
            row, op = row[:-1], row[-1]
        nums.append(int(row))

r2 += sum(nums) if op == '+' else prod(nums)

print(r1, r2)
