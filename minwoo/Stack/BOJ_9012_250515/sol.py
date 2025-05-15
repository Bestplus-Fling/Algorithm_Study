import sys
sys.stdin = open('input.txt', 'r')


def f(text):
    stack = []
    # N = len(text)
    for i in text:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return 'NO'
            stack.pop()
    if stack:
        return 'NO'
    return 'YES'


T = int(input())
for t in range(T):
    print(f(list(input().strip())))
