with open('data.txt') as f:
    contents = f.read().split()
    gdata = [str(int(sum([int(j[i]) for j in contents]) > len(contents)/2)) for i in range(len(contents[0]))]
    edata = [str(int(sum([int(j[i]) for j in contents]) < len(contents)/2)) for i in range(len(contents[0]))]

gamma = int(''.join(gdata), base=2)
epsilon = int(''.join(edata), base=2)
print(gamma * epsilon)