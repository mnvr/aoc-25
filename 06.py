import sys
from math import prod
import re

nums = None
# nums = [[0]*3 for _ in range(0, 4)]
# nums = [list([] for _ in range(0, 3)) for _ in range(0, 4) ]
# print(nums)
result = 0
for line in sys.stdin:
    print(line)
    if nums is None:
        nums = []
        count = 0
        # if line[-1] == '\n':
            # line = line[:-1]
        for (i, c) in enumerate(line):
            print(i, c, count, end=': ')
            if c == ' ' and i > 0 and line[i-1] != ' ':
                print('append to nums')
                nums.append(list([[] for _ in range(0, count)]))
                count = 0
            else:
                print('incr count')
                count += 1
        nums.append(list([[] for _ in range(0, count)]))

    print(nums)
    exit()

    if line[-1] == '\n':
        line = line[:-1]
    if nums is None:
        nums = []
        count = 0
        for (i, c) in enumerate(line):
            if c == ' ' and i+1 < len(line) and line[i+1] != ' ':
                nums.append(list([[] for _ in range(0, count)]))
                count = 0
    elif line[0] in ['+', '*']:
        for (i, s) in enumerate(line.split()):
            match s:
                case '+': result += sum(nums[i])
                case '*': result += prod(nums[i])
    else:
        print(nums)
        a, b = 0, 0
        for (i, c) in enumerate(line):
            if c != ' ':
                nums[a][b].append(int(c))
                b += 1
            else:
                if i+1 < len(line) and line[i+1] != ' ':
                    nums[a][b].append(int(c))
                    b += 1
                else:
                    b = 0
                    a += 1

    print(nums)
    continue

    for (i, s) in enumerate(line.split()):
        print(nums)
        match s:
            case '+': result += sum(nums[i])
            case '*': result += prod(nums[i])
            case _:
                for (j, c) in enumerate(reversed(s)):
                    # print(i, j, c, nums)
                    nums[i][j].append(int(c))
                    # nums[i][j] = nums[i][j]*10 + int(c)
    # print(nums)
    # exit()

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
