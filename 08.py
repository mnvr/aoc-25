import sys

boxes = [list(map(int, line.split(','))) for line in sys.stdin]
for box in boxes:
    print(box)
