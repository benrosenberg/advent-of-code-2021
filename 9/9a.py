with open('data.txt') as f:
    data = [line.rstrip('\n') for line in f.readlines()]

print(data)

def surroundings(data, point):
    r,c = point
    above = data[r-1][c] if r > 0 else -1
    below = data[r+1][c] if r < (len(data)-1) else -1
    left = data[r][c-1] if c > 0 else -1
    right = data[r][c+1] if c < (len(data[0])-1) else -1
    adjacent = (left, right, above, below)
    return [a for a in adjacent if a != -1]

low_points = []
for i in range(len(data)):
    for j in range(len(data[0])):
        adj = surroundings(data, (i,j))
        if all(a > data[i][j] for a in adj):
            low_points.append(int(data[i][j]))

print(low_points)
print(sum(low_points) + len(low_points))