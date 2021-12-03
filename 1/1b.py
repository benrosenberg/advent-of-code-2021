from typing import List

def puzzle(arr: List) -> int:
    # count number of times depth increases from one group of three measurements to the next
    group_sums = [sum(arr[i:i+3]) for i in range(0, len(arr))]
    print(group_sums)
    increases = [int(group_sums[i] > group_sums[i-1]) for i in range(1, len(group_sums))]
    return sum(increases)

with open('report.txt') as f:
    data = [int(line) for line in f.readlines()]

# data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print(puzzle(data))
