import sys
sys.stdin = open('input.txt', 'r')
#########################################


'''
0 성별, 1 학년
0 여학생
1 남학생
'''

n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ban = [[0] * 7 for _ in range(2)]
result = 0
a = 0
for i in range(n):
    ban[arr[i][0]][arr[i][1]] += 1
    a = max(a, arr[i][1])

for i in range(len(ban)):
    for j in range(7):
        # if ban[i][j] % k != 0:
        result += (ban[i][j] + k - 1) // k
        # else:
        #     result += ban[i][j] // k

print(result)



