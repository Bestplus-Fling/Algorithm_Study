import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = 8
data = [list(input().strip()) for _ in range(N)]
C = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 'F' and C == 0:
            cnt += 1
        C = (C + 1) % 2
    C = (C + 1) % 2
print(cnt)

