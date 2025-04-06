import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
체스판을 8x8로 잘라서 칠해야함

이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다
'''



def count(x, y, start):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0: # 홀짝
                if data[x + i][y + j] != start: # 짝수는 같아야되는데 다르면 +1
                    cnt += 1
            else:
                if data[x + i][y + j] == start: # 홀수는 달라야됨
                    cnt += 1
    return cnt


n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]

min_cnt = float('inf')
for i in range(n - 7): # 범위 지정
    for j in range(m - 7):
        min_cnt = min(min_cnt, count(i, j, 'W'), count(i, j, 'B'))

print(min_cnt)

