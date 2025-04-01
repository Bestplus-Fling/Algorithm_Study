import sys
sys.stdin = open("10163. 색종이.txt", "r")


arr = [[0] * 1001 for _ in range(1001)]

N = int(input())


for colorpaper in range(1, N + 1):
    # 입력 받기/ 가장 왼쪽 칸의 번호와 너비, 높이
    x, y, w, h = map(int, input().split())
    # 행 좌표  ~ 행 좌표 + 너비
    for i in range(x, x + w):
        # 열 좌표 ~ 열 좌표 + 높이
        for j in range(y, y + h):
            # 해당하는 배열은 색종이 칸임!
            arr[i][j] = colorpaper

# n장의 색종이
for colorpaper in range(1, N + 1):
    w_h = 0
    # 배열 탐색해서 색종이인 부분은 w_h에 더해줌
    for search in arr:
        for pick in search:
            if pick == colorpaper:
                w_h += 1

    print(w_h)
