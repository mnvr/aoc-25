import sys

mx = []
for line in sys.stdin:
    mx.append([0 if c == '.' else 1 for c in line.strip()])

print(mx)
