import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
commend = [int(input()) for _ in range(N)]
queue = []
for cmd in commend:
    if cmd == 0:
        if not queue:
            print(0)
            continue
        print(-(heapq.heappop(queue)))
    else:
        heapq.heappush(queue, -cmd)
