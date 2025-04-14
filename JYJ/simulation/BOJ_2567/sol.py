import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
둘레를 어케 구하는데


델타? 돌려서 0찾으면 제일 바깥이라는 거니까
+1
'''
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

n = int(input())
arr = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(n):
    x, y = map(int,input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy

                if not(0 <= ni < 101 and 0 <= nj < 101): continue

                if arr[ni][nj] == 1: continue

                if arr[ni][nj] == 0:
                    cnt += 1

print(cnt)
