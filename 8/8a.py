from functools import reduce

with open('data.txt') as f:
    data = [i[:-1].split(' | ') for i in f.readlines()]

easy_num_lengths = {
    2 : 1,
    3 : 7,
    4 : 4,
    7 : 8
}


splitlengths = [[[len(k) for k in j.split(' ')] for j in d] for d in data]
# right = [[j[1] for j in i] for i in splitlengths]
right = [i[1] for i in splitlengths]
flatright = reduce(lambda x,y:x+y, right)
easy_counts = [flatright.count(i) for i in easy_num_lengths]
print(sum(easy_counts))

print(easy_counts)

