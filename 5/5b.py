from itertools import chain

with open('data.txt') as f:
    data = [[tuple(map(int, j.split(','))) for j in i.replace('\n', '').split(' -> ')] 
                                           for i in f.readlines()]

def diag(a,b):
    return abs(a[0] - b[0]) == abs(a[1] - b[1])

def lines_from_points(a, b): 
    if a[0] != b[0] and a[1] != b[1] and not diag(a,b): # take h, v, d lines
        return []
    
    if a[0] == b[0]:
        return [(a[0], i) for i in range(min(a[1], b[1]), max(a[1], b[1])+1)]
    elif a[1] == b[1]:
        return [(i, b[1]) for i in range(min(a[0], b[0]), max(a[0], b[0])+1)]
    else:
        return [i for i in zip(range(a[0], b[0]+1-2*int(a[0]>b[0]), -1+2*int(a[0]<b[0])), 
                               range(a[1], b[1]+1-2*int(a[1]>b[1]), -1+2*int(a[1]<b[1])))]

points = chain(*[lines_from_points(*line) for line in data])
counts = {}
for i in points: counts[i] = counts.get(i, 0) + 1

print(sum(i > 1 for i in counts.values()))