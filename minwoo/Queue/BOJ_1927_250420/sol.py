import sys
import heapq
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N = int(input())
queue = []
_len = 0
for i in range(N):
    num = input().strip()
    if num == '0':
        if _len == 0:
            print(0)
        else:
            print(str(heapq.heappop(queue)))
            _len -= 1
    else:
        heapq.heappush(queue, int(num))
        _len += 1
