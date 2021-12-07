from collections import Counter

with open('data.txt') as f:
    data = [int(i) for i in f.read().split(',')]
    fish = [i for i in data]

c = Counter(fish)

days = 256
for day in range(days):
    temp = [c[i] for i in range(9)]
    c[8] = c[0]; temp[7] += c[0]
    for i,x in list(enumerate(temp))[1:]: c[i-1] = x

print(c.total())

def fish(inp, days):
    c = Counter(inp)
    for _ in range(days):
        temp = [c[i] for i in range(9)]
        c[8] = c[0]; temp[7] += c[0]
        for i,x in list(enumerate(temp))[1:]: c[i-1] = x
    return c.total()