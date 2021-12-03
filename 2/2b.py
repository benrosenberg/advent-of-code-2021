with open('data.txt') as f:
    data = [(j[0], int(j[1])) for j in [i.split(' ') for i in f.readlines()]]
    
todo = {
    'forward'  : lambda x, aim: (complex(x, aim * x), aim),
    'backward' : lambda x, aim: (complex(-x, 0), aim),
    'up'       : lambda x, aim: (complex(0, 0), aim - x),
    'down'     : lambda x, aim: (complex(0, 0), aim + x)
}

new = [todo[data[0][0]](data[0][1], 0)]
i = 1
while i < len(data):
    new.append(todo[data[i][0]](data[i][1], new[i-1][1]))
    i += 1

sums = sum([i[0] for i in new])

print(sums.real * sums.imag)