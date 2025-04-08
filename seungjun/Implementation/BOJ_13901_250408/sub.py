import sys

input = sys.stdin.readline
print = sys.stdout.write


def jihun_bfs(r, c, maze, fire, jihun):
    dis = 0
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while jihun:
        dis += 1

        tmp_fire = []
        for y, x in fire:
            for dy, dx in direction:
                ny, nx = dy + y, dx + x
                if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] == ".":
                    maze[ny][nx] = "F"
                    tmp_fire.append((ny, nx))
        fire = tmp_fire

        tmp_jihun = []
        for y, x in jihun:
            for dy, dx in direction:
                ny, nx = dy + y, dx + x
                if 0 <= ny < r and 0 <= nx < c:
                    if maze[ny][nx] == ".":
                        maze[ny][nx] = "J"
                        tmp_jihun.append((ny, nx))
                else:
                    return dis
        jihun = tmp_jihun
    return "IMPOSSIBLE"


def main():
    r, c = map(int, input().split())
    jihun = list()
    fire = list()
    maze = []
    for i in range(r):
        maze.append(list(input().rstrip()))
        for j in range(c):
            if maze[-1][j] == "J":
                jihun.append((i, j))
            elif maze[-1][j] == "F":
                fire.append((i, j))

    print(f"{jihun_bfs(r, c, maze, fire, jihun)}")


if __name__ == "__main__":
    main()
