import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0

def left(d):
    return (d + 3) % 4

while True:
    # 현재 위치가 청소되지 않았으면 청소
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1

    cleaned = False

    # 4방향 확인
    for _ in range(4):
        d = left(d)  # 왼쪽 방향으로 회전


        if d == 0:    # 북
            nx, ny = r - 1, c
        elif d == 1:  # 동
            nx, ny = r, c + 1
        elif d == 2:  # 남
            nx, ny = r + 1, c
        else:         # 서
            nx, ny = r, c - 1


        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    # 후진
    if not cleaned:
        if d == 0:    # 북의 반대 → 남
            back_r, back_c = r + 1, c
        elif d == 1:  # 동의 반대 → 서
            back_r, back_c = r, c - 1
        elif d == 2:  # 남의 반대 → 북
            back_r, back_c = r - 1, c
        else:         # 서의 반대 → 동
            back_r, back_c = r, c + 1

        if 0 <= back_r < N and 0 <= back_c < M and arr[back_r][back_c] != 1:
            r, c = back_r, back_c
        else:
            break

print(cnt)
