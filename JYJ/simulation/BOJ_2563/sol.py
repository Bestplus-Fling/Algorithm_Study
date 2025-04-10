import sys
sys.stdin = open('input.txt', 'r')
#########################################


'''

'''


n = int(input())



arr = [[0] * 101 for _ in range(101)]
result = 0
for k in range(n):
    sekjong_ex, sekjong_ey = map(int,input().split())

    for i in range(sekjong_ex, sekjong_ex + 10):
        for j in range(sekjong_ey, sekjong_ey + 10):
            arr[i][j] = 1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            result += 1

print(result)



