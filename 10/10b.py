with open('data.txt') as f:
    data = [line.rstrip('\n') for line in f.readlines()]

open_close = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}

scores = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

def syntax_error_score(line):
    stack = []
    pointer = 0
    while pointer < len(line):
        if stack == []:
            stack.append(line[pointer])
            pointer += 1
            continue
        if line[pointer] in open_close:
            stack.append(line[pointer])
            pointer += 1
            continue
        if open_close[stack[-1]] == line[pointer]:
            stack.pop()
            pointer += 1
            continue
        if open_close[stack[-1]] != line[pointer] and line[pointer] in scores:
            return scores[line[pointer]], None
        pointer += 1
    
    return [0, stack]

errs = [syntax_error_score(line)[1] for line in data if syntax_error_score(line)[0] == 0]

def fix_err(err):
    return [open_close[e] for e in err][::-1]

err_char_score = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

def score_err(fix):
    total_score = 0
    for char in fix:
        total_score *= 5
        total_score += err_char_score[char]
    return total_score

scores = sorted([score_err(fix_err(x)) for x in errs])

print(scores[(len(scores)//2)])