import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
n을 5로 나눈 값이 0이면 입력 그대로 출력
1이 아니고 홀수일 경우 초기 입력에서 터진 거 출력
짝수일 경우 꽉찬 배열 출력

'''

def printing(arr):
    for a in arr:
        print(''.join(map(str,a)))


dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]

r, c, n = map(int,input().split())

arr = [list(input()) for _ in range(r)]
holsu = [['O'] * c for _ in range(r)]
jjaksu = [['O'] * c for _ in range(r)]


for i in range(r):
    for j in range(c):
        if arr[i][j] == "O":
            holsu[i][j] = '.'
            for dx, dy in dxy:
                ni = i + dx
                nj = j + dy

                if not(0 <= ni < r and 0 <= nj < c): continue

                holsu[ni][nj] = '.'


if n % 5 == 0 or n % 5 == 1:  # << 여기 모르겠습니다 조건문
    printing(arr)
elif (n % 5) % 2 != 0:
    printing(holsu)
else:
    printing(jjaksu)

