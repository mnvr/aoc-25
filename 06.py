import sys

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
