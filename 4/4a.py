from functools import reduce

with open('data.txt') as f:
    drawing = [int(x) for x in f.readline()[:-1].split(',')]
    board_raw = f.read()[1:].split('\n\n')

boards = [[[int(x) for x in l.split()] for l in board.split('\n')] for board in board_raw]

def has_won(board, drawn_so_far):
    n = len(board)
    cols = sum(sum(board[j][k] in drawn_so_far for j in range(n)) == 5 for k in range(n)) > 0 
    rows = sum(sum(i in drawn_so_far for i in row) == 5 for row in board) > 0
    return cols or rows

i = 0; won = []
while sum(won) == 0: i += 1; won = [int(has_won(b, drawing[:i])) for b in boards]

winners = [j for j,e in enumerate(won) if e]
winning_sum = sum(j for j in reduce(lambda x,y: x+y, boards[winners[0]]) if j not in drawing[:i])

print(f'last called * winning sum = {drawing[i-1] * winning_sum}')

'''DEBUG''' """
def draw_board(board, highlight):
    for j in range(5): 
        print('[', end=' ')
        for k in range(5):
            print(' ', end='')
            if (x := board[j][k]) in highlight:
                print(f'>{x}<', end='\t')
            else: print(x, end='\t')
        print(']')

for j, board in enumerate(boards):
    print(j)
    draw_board(board, highlight = drawing[:i])

print(f'winners: {winners}')
print('winning board:');
draw_board(boards[winners[0]], drawing[:i])
print('drawn so far:', drawing[:i])
print(f'winning sum is {winning_sum}')
print(f'last called is {drawing[i-1]}')
print(f'last called * winning sum = {drawing[i-1] * winning_sum}')
'''DEBUG''' """