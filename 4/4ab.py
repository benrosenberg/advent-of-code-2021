from itertools import chain

with open('data.txt') as f:
    drawing = [int(x) for x in f.readline()[:-1].split(',')]
    board_raw = f.read()[1:].split('\n\n')

boards = [[[int(x) for x in l.split()] for l in board.split('\n')] for board in board_raw]

def has_won(board, drawn_so_far):
    n = len(board)
    cols = sum(sum(board[j][k] in drawn_so_far for j in range(n)) == 5 for k in range(n)) > 0 
    rows = sum(sum(i in drawn_so_far for i in row) == 5 for row in board) > 0
    return cols or rows

i = 0; won = []; diff = []; flag = 0
while sum(won) < len(boards): 
    i += 1; temp = won
    won = [int(has_won(b, drawing[:i])) for b in boards]
    diff = [k for k,(w,t) in enumerate(zip(temp,won)) if w-t]
    if sum(won) == 1 and flag < 1: winner = diff[0]; flag = i

winning_sum = sum(j for j in chain(*boards[winner]) if j not in drawing[:flag])
losing_sum = sum(j for j in chain(*boards[diff[0]]) if j not in drawing[:i])

print(f'(a) last called * winning sum \t= {drawing[flag-1] * winning_sum}')
print(f'(b) last called * losing sum \t= {drawing[i-1] * losing_sum}')