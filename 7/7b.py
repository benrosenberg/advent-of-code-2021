import numpy as np
with open('data.txt') as f:
    data = np.array([int(i) for i in f.read().split(',')])

tryrange = range(min(data), max(data))

def cumsum(n): 
    return sum(range(n+1))

print(min(np.sum(list(map(cumsum, abs(data - t)))) for t in tryrange))