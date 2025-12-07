import sys
from math import prod

def to_num(xs):
    n = 0
    for x in xs:
        n = n * 10 + x
    return n

nums = None
result = 0
for line in sys.stdin:
    print(line)
    if nums is None:
        nums = []
        count = 0
        i = 0
        while i < len(line):
            while i < len(line) and line[i] == ' ':
                i += 1
                count += 1
            if i < len(line):
                while i < len(line) and line[i] != ' ':
                    i += 1
                    count += 1
                print("num len", count)
                nums.append(list([[] for _ in range(0, count)]))
                count = 0
                i += 1

    if line[0] in ['+', '*']:
        for (i, s) in enumerate(line.split()):
            print(nums[i])
            match s:
                case '+': result += sum(map(to_num, nums[i]))
                case '*': result += prod(map(to_num, nums[i]))
    else:
        a, b = 0, 0
        for c in line:
            if c != ' ' and c != '\n':
                nums[a][b].append(int(c))
            b += 1
            if b > len(nums[a]):
                b = 0
                a += 1

    print(nums)

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
