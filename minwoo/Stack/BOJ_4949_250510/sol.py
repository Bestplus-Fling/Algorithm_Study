import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
opn = ['[', '(']
cls = [']', ')']
dic = {')': '(', ']': '['}


def check(txt):
    global opn, cls, dic
    stack = []
    for t in txt:
        if t in opn:
            stack.append(t)
        if t in cls:
            if stack and dic[t] == stack[-1]:
                stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'


while True:
    text = input().rstrip()
    # print(text)
    if text[0] == '.':
        break
    print(check(text))
