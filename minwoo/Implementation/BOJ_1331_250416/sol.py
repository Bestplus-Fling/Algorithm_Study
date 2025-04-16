import sys
sys.stdin = open("input.txt", "r")

dxy = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def brute_force():
    global coordinate, K, N
    visited = set()
    visited.add(coordinate[0])
    bx, by = coordinate[0]
    for x, y in coordinate[1::]:
        if (x, y) in visited:
            return 'Invalid'
        if (abs(bx-x), abs(by-y)) not in [(1, 2), (2, 1)]:
            return 'Invalid'
        visited.add((x, y))
        bx, by = x, y
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx, ny) == coordinate[0]:
            return 'Valid'
    return 'Invalid'


N = 6
K = 36
coordinate = []
dicA = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
for _ in range(K):
    a, b = list(input().strip())
    coordinate.append((dicA[a], int(b)-1))

print(brute_force())