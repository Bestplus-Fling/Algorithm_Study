# https://www.acmicpc.net/problem/16953

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def f(x, y):
    queue = deque([(x, 1)])
    while queue:
        n, cnt = queue.popleft()
        if n == y:
            return cnt
        cnt += 1
        case1 = (n*10)+1
        if case1 <= y:
            queue.append((case1, cnt))
        case2 = n * 2
        if case2 <= y:
            queue.append((case2, cnt))
    return -1


A, B = map(int, input().split())
print(f(A, B))
