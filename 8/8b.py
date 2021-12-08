from functools import reduce

with open('data.txt') as f:
    data = [i[:-1].split(' | ') for i in f.readlines()]

easy_lengths = {
    2 : 1,
    3 : 7,
    4 : 4,
    7 : 8
}

num_segments = {
    0 : (0, 1, 2, 4, 5, 6),
    1 : (2, 5),
    2 : (0, 2, 3, 4, 6),
    3 : (0, 2, 3, 5, 6),
    4 : (1, 2, 3, 5),
    5 : (0, 1, 3, 5, 6),
    6 : (0, 1, 3, 4, 5, 6),
    7 : (0, 2, 5),
    8 : (0, 1, 2, 3, 4, 5, 6),
    9 : (0, 1, 2, 3, 5, 6)
}

rev_num_segments = {v:k for (k,v) in num_segments.items()}

'''LOGIC''' """

 0000
1    2
1    2
 3333
4    5
4    5
 6666
let c be a character.
if c is in both 1 and 7, then it's either 2 or 5
if c is in 4 but not 1 or 7, then it's either 1 or 3
if c is in 7 but not 1, then it's 0
if c is in 8 but not 7 or 4, then it's either 4 or 6
3 is present in all 5-length strings and in 4 
if the length of a string is 6 and it has 0, 2, 3, and 5 in it, it must be 9 -> 4 is missing from it
    (so we can get 6 by process of elimination from before)
otherwise, if the length is 6 and it has 0 but only one of 2 or 5, it must be 6, which has 2 missing
    (so we can get 5 by process of elimination from before)
lastly we can get 1 by POE from previous results
"""

def overlap_parser(nums, easy_nums):
    flat_first_easy = [x[0] for x in easy_nums]
    potentials = {}
    one_chars = flat_first_easy[0][1] # 1
    # print('one chars', one_chars)
    sev_chars = flat_first_easy[1][1] # 7
    # print('sev chars', sev_chars)
    zero = list(set(sev_chars) - set(one_chars))[0]
    potentials[(2,5)] = list(set(sev_chars) & set(one_chars))
    four_chars = flat_first_easy[2][1] # 4
    # print('four chars', four_chars)
    potentials[(1,3)] = list(set(four_chars) - set(sev_chars))
    eight_chars = flat_first_easy[3][1] # 8
    # print('eight chars', eight_chars)
    potentials[(4,6)] = list(set(eight_chars) - (set(four_chars) | set(sev_chars)))
    # print('nums', nums)
    fives = [x for x in nums if len(x) == 5]
    THREE = set(fives[0])
    for num in fives:
        THREE &= (set(num) - {zero})
    THREE &= set(four_chars)
    three = list(THREE)[0]
    for num in nums:
        if len(num) == 6:
            if all(i in num for i in set(potentials[(2,5)]) | {zero}): # could be zero or 9
                if three in num: # must be 9
                    four = list(set(eight_chars) - set(num))[0]
                    six = list(set(potentials[(4,6)]) - {four})[0]
            elif zero in num and any(i in num for i in potentials[(2,5)]): # must be 6
                two = list(set(eight_chars) - set(num))[0]
                five = list(set(potentials[(2,5)]) - {two})[0]
    one = list(set(eight_chars) - set([zero, two, three, four, five, six]))[0]
    # print('potentials', potentials)
    # print('zero', zero, 'one', one, 'two', two, 'three', three, 'four', four, 'five', five, 'six', six)
    arrangement = {
        zero    : 0,
        one     : 1,
        two     : 2,
        three   : 3,
        four    : 4,
        five    : 5,
        six     : 6
    }
    # print('arrangement:',arrangement)
    return arrangement

def number(l, arrangement):
    split = l.split(' ')
    # print(split)
    unique_char_lists = [list(s) for s in split]
    # print(unique_char_lists)
    rns = [tuple(sorted(arrangement[x] for x in q)) for q in unique_char_lists]
    # print(rns)
    return [rev_num_segments[p] for p in rns]

# determine where easy num lengths correspond to
def convert(line):
    left, right = line
    entire_string = left + ' ' + right
    charsets = entire_string.split(' ')
    easy_nums = [[(j,i) for i in charsets if (len(i) in easy_lengths) and easy_lengths[len(i)] == j] 
                    for j in [1,7,4,8]]
    # print('charsets:',charsets)
    nums = [i for i in charsets if (len(i) not in easy_lengths)]
    # print(easy_nums)
    arrangement = overlap_parser(nums, easy_nums)
    digits = [str(i) for i in number(right, arrangement)]
    digits = reduce(lambda x,y:x+y, digits)
    # print(digits)
    return int(digits)

# print(data)
print(convert(['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab', 'cdfeb fcadb cdfeb cdbaf']))
# print(convert(data[0]))

print(sum(convert(line) for line in data))
# print(data)



