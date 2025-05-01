import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())
tower = [(j, i+1) for i, j in enumerate(list(map(int, input().split())))]
ans = ['0'] * N
idx = 0
stack = []
for top in tower:
    while stack:
        if stack[-1][0] <= top[0]:
            stack.pop()
        else:
            ans[top[1]-1] = str(stack[-1][1])
            break
    stack.append(top)
print(' '.join(ans))
