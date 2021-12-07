import numpy as np
with open('data.txt') as f:
    data = np.array([int(i) for i in f.read().split(',')])

tryrange = range(min(data), max(data))

print(min(np.sum(list(map(int, abs(data - t)))) for t in tryrange))