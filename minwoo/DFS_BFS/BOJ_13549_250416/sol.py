import sys
sys.stdin = open('input.txt', 'r')


def bfs():
    global N, K
    if N == K:
        return 0
    queue = [(N, 0)]
    visited = set()
    visited.add(N)
    while queue:
        temp = []
        for x, t in queue:
            if x * 2 <= 100000 and x*2 not in visited:
                if x * 2 == K:
                    return t
                temp.append((x * 2, t))
                visited.add(x*2)
            if x - 1 >= 0 and x-1 not in visited:
                if x - 1 == K:
                    return t + 1
                temp.append((x - 1, t + 1))
                visited.add(x-1)
            if x + 1 <= 100000 and x+1 not in visited:
                if x + 1 == K:
                    return t + 1
                temp.append((x + 1, t + 1))
                visited.add(x+1)
        queue = temp


N, K = map(int, input().split())
print(bfs())