import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
commend = [int(input()) for _ in range(N)]
queue = []
for cmd in commend:
    if cmd == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, (abs(cmd), cmd))
