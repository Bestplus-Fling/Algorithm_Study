import sys
sys.stdin = open('input.txt', 'r')
#########################################

import sys
input = sys.stdin.readline


n = int(input())
stack = []
order = [list(map(int,input().split())) for _ in range(n)]
result = [0] * 1000000
cnt = 0
for i in range(n):
    if order[i][0] == 4:
        if not stack:
            result[i - cnt] = 1
        else:
            result[i - cnt] = 0
    elif order[i][0] == 3:
        result[i - cnt] = len(stack)

    elif order[i][0] == 2:
        if stack:
            result[i - cnt] = stack.pop()
        else:
            result[i - cnt] = -1
    elif order[i][0] == 5:
        if stack:
            result[i - cnt] = stack[-1]
        else:
            result[i - cnt] = -1

    elif order[i][0] == 1:
        stack.append(order[i][1])
        cnt += 1


for i in range(n - cnt):
    print(result[i])



