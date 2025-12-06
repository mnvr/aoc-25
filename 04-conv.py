import sys

papers = {(x, y) for y,r in enumerate(sys.stdin)
                 for x,c in enumerate(r) if c == '@'}

def prune(papers):
    new = papers.copy()
    for (x, y) in papers:
        neighbours = {(i,j) for i in [x-1, x, x+1] for j in [y-1, y, y+1]}
        if len(papers & neighbours) <= 4:
            new.remove((x, y))
    return new

s = []
while len(new := prune(papers)) != len(papers):
    s.append(len(papers) - len(new))
    papers = new

print(s[0], sum(s))
