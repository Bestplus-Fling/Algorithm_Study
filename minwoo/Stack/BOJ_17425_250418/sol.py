import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    case = input().split()
    if case[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif case[0] == 'size':
        print(len(stack))
    elif case[0] == 'empty':
        print(0 if stack else 1)
    elif case[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif case[0] == 'push':
        stack.append(case[1])
