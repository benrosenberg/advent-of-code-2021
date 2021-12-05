from itertools import chain

with open('data.txt') as f:
    data = [[tuple(map(int, j.split(','))) for j in i.replace('\n', '').split(' -> ')] 
                                           for i in f.readlines()]

def lines_from_points(a, b): 
    # returns LIST of TUPLES (int, int) that are covered by line from point A to point B
    if a[0] != b[0] and a[1] != b[1]:
        return []
    if a[0] == b[0]:
        return [(a[0], i) for i in range(min(a[1], b[1]), max(a[1], b[1])+1)]
    else:
        return [(i, b[1]) for i in range(min(a[0], b[0]), max(a[0], b[0])+1)]

points = chain(*[lines_from_points(*line) for line in data])
counts = {}
for i in points: counts[i] = counts.get(i, 0) + 1

print(sum(i > 1 for i in counts.values()))

'''DEBUG''' """
for i in range(10):
    for j in range(10):
        if (j,i) in counts:
            print(counts[(j,i)], end='')
        else:
            print('.', end='')
    print()
'''DEBUG''' """