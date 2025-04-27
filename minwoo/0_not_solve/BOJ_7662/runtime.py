import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def priority_queue(commend):
    q = []
    for cmd in commend:
        x, num = cmd
        num = int(num)
        if x == 'I':
            heapq.heappush(q, num)
        elif q:
            if x == 'D' and num == 1:
                max_value = max(q)
                q.remove(max_value)
            else:
                heapq.heappop(q)
    if q:
        return [max(q), heapq.heappop(q)]
    return []


for t in range(int(input())):
    K = int(input())
    result = priority_queue([input().split() for _ in range(K)])
    if result:
        print(*result)
    else:
        print('EMPTY')
