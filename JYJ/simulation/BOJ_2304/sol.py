import sys

sys.stdin = open("input.txt", "r")
##########################################

'''

x 좌표를 기준으로 정렬
가장 높은 기둥을 만날 때 까지 넓이 더하고
뒤에서 부터 순회하면서 또 가장 높은 기둥을 만날 때 까지 순회

그후 마지막으로 가장 높은 기둥의 면적 더하기


'''



n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort()
result = 0
hi = 0
cnt = 1
idx = 0
d = 0
for i in range(n):
    if hi < arr[i][1]:
        hi = arr[i][1]
        idx = arr[i][0]
        d = i

left_h = arr[0][1]
a1 = arr[0][0]
for i in range(n):
    if left_h == hi:
        break
    if arr[i][1] >= left_h:
        result += left_h * (arr[i][0] - a1)
        left_h = arr[i][1]
        a1 = arr[i][0]


arr.reverse()
right_h = arr[0][1]
a2 = arr[0][0]
for i in range(n):
    if right_h == hi:
        break
    if arr[i][1] >= right_h:
        result += right_h * (a2 - arr[i][0])
        right_h = arr[i][1]
        a2 = arr[i][0]


# idx = hi 의 인덱스
arr.sort()
for i in range(d, n):
    if arr[i][1] == hi:
        cnt = abs(arr[i][0] - idx) + 1


result += hi * cnt
print(result)

