from itertools import chain

with open('small.txt') as f:
    data = [[tuple(map(int, j.split(','))) for j in i.replace('\n', '').split(' -> ')] 
                                           for i in f.readlines()]

def diag(a,b):
    return abs(a[0] - b[0]) == abs(a[1] - b[1])

def lines_from_points(a, b, diags=False): 
    hv = a[0] == b[0] or a[1] == b[1]
    if (diags and (not diag(a,b) and not hv)) or not (diags or hv):
        return []
    if diags and not hv:
        return [i for i in zip(range(a[0], b[0]+1-2*int(a[0]>b[0]), -1+2*int(a[0]<b[0])), 
                               range(a[1], b[1]+1-2*int(a[1]>b[1]), -1+2*int(a[1]<b[1])))]
    if a[0] == b[0]:
        return [(a[0], i) for i in range(min(a[1], b[1]), max(a[1], b[1])+1)]
    else:
        return [(i, b[1]) for i in range(min(a[0], b[0]), max(a[0], b[0])+1)]

nd_points, d_points = (chain(*[lines_from_points(*line) for line in data]),
                       chain(*[lines_from_points(*line, diags=True) for line in data]))
nd_counts, d_counts = {}, {}
for i in nd_points: nd_counts[i] = nd_counts.get(i, 0) + 1
for i in d_points: d_counts[i] = d_counts.get(i, 0) + 1

print(f'(a): {sum(i > 1 for i in nd_counts.values())}')
print(f'(b): {sum(i > 1 for i in d_counts.values())}')