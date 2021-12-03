with open('data.txt') as f:
    data = [(j[0], int(j[1])) for j in [i.split(' ') for i in f.readlines()]]
    
todo = {
    'forward'  : lambda x: complex(x[1], 0),
    'backward' : lambda x: complex(-x[1], 0),
    'up'       : lambda x: complex(0, -x[1]),
    'down'     : lambda x: complex(0, x[1])
}

data = [todo[x[0]](x) for x in data]

sums = sum(data)

print(sums.real * sums.imag)
