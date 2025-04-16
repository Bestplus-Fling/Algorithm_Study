import sys
sys.stdin = open('input.txt', 'r')


def bfs():
    global N, K
    queue = [K]
    cnt, time = 0, 0
    while queue:
        temp = []
        if cnt != 0:
            return time, cnt
        for x in queue:
            if x * 2 <= 100000:
                temp.append(x*2)
                if x * 2 == N:
                    cnt += 1
            if x - 1 >= 0:
                temp.append(x-1)
                if x - 1 == N:
                    cnt += 1
            if x + 1 <= 100000:
                temp.append(x+1)
                if x + 1 == N:
                    cnt += 1
        queue = temp
        time += 1


N, K = map(int, input().split())
print(*bfs(), sep='\n')