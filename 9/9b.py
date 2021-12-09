with open('data.txt') as f:
    data = [line.rstrip('\n') for line in f.readlines()]

# print(data)

def surroundings(data, point): # now returns indices instead of values
    r,c = point
    above = (r-1,c) if r > 0 else -1
    below = (r+1,c) if r < (len(data)-1) else -1
    left = (r,c-1) if c > 0 else -1
    right = (r,c+1) if c < (len(data[0])-1) else -1
    adjacent = (left, right, above, below)
    return [a for a in adjacent if a != -1]

def flatten(nested):
    out = []
    for item in nested:
        if type(item) == list:
            if item == []:
                continue
            else:
                # print(f'flattening type {type(item)}')
                out += flatten(item)
        else:
            out.append(item)
    return out

def get(data, u):
    return data[u[0]][u[1]]

def pretty_print_basin(data, basin):
    for i in range(len(data)):
        print('[', end='\t')
        for j in range(len(data[0])):
            if (i,j) in basin:
                print(f'>{data[i][j]}<', end='\t')
            else:
                print(data[i][j], end='\t')
        print(']', end='\n')

def total_surroundings(data, basin_start_point, visited):
    visited.add(basin_start_point)
    adjacent = surroundings(data, basin_start_point)
    unvisited = list(set(adjacent) - visited)
    if len(unvisited) == 0: # all are already visited
        return None
    if all(u == '9' for u in unvisited): # reached an edge
        return None
    non_nines = [u for u in unvisited if get(data, u) != '9']
    unvisited_surroundings = [total_surroundings(data, u, visited) for u in non_nines]
    unvisited_surroundings = [us for us in unvisited_surroundings if us is not None]
    # print(unvisited_surroundings)
    visited |= set(non_nines)
    # print(len(visited))
    return flatten(non_nines + unvisited_surroundings)

def find_basins(data):
    # idea: recursively check surroundings to see whether they are inside the basin or not.
    # if an elt is 9 then it is not in the basin associated with our check.
    # basically, dfs, kinda
    basins = [] # will be nested list 
    # [[(x11,y11), (x12,y12), ..., (x1n,y1n)], [(x21,y21), (x22,y22), ..., (x2n,y2n)], ..., etc.]
    all_points = set()

    total_nines = (''.join(data)).count('9')
    # print(total_nines)
    total_points = len(''.join(data))
    # print(total_points)

    # while we haven't visited all points...
    num_basins = 0
    while len(all_points) < total_points - total_nines:
        # find new basin
        found = False
        # remaining_points = 
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] != '9' and (i,j) not in all_points:
                    found = True
                    basin_start_point = (i,j)
                if found:
                    break
            if found:
                break

        this_visited = set()
        new_basin = list(set(total_surroundings(data, basin_start_point, this_visited) 
                             + [basin_start_point]))
        basins.append(new_basin)

        all_points |= set(new_basin)

        num_basins += 1
        print(f'num_basins: {num_basins}')

    # print(basins)

    return basins

basins = find_basins(data)

# for b in basins: 
#     print(b)
#     pretty_print_basin(data, b)

basin_lengths = [(len(basin),basin) for basin in basins]
sorted_basins = sorted(basin_lengths, key=lambda x:x[0], reverse=True)

top_three = sorted_basins[:3]

# for b in sorted_basins:
#     print(b)
#     pretty_print_basin(data, b[1])

out = top_three[0][0] * top_three[1][0] * top_three[2][0]

print(out)