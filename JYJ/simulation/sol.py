import sys

sys.stdin = open("input.txt", "r")
##########################################

'''

그냥 크면 1 더하셈 개빡치게 하지말고


'''

n = int(input())
dc = []
for i in range(n):
    weight, height = map(int, input().split())
    dc.append((weight, height))

arr = [1] * n
# 키는 같은데 몸무게가 다른경우 수정해야됨

for i in range(n):
    for j in range(n):
        if i == j: continue

        if dc[i][0] < dc[j][0] and dc[i][1] < dc[j][1]:
            arr[i] += 1


print(*arr)