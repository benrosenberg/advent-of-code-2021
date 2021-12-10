with open('small.txt') as f:
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
            return scores[line[pointer]]
        pointer += 1
        print(f'stack is {stack}')
    
    return 0

print(sum(syntax_error_score(line) for line in data))