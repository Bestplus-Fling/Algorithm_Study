# https://www.acmicpc.net/problem/16953

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def f(x, y):
    queue = deque([(y, 1)])
    while queue:
        n, cnt = queue.popleft()
        if n == x:
            return cnt
        cnt += 1
        if n % 10 != 1:
            case1 = n // 2
            if case1 >= x:
                queue.append((case1, cnt))
        else:
            case2 = n // 10
            if case2 >= x:
                queue.append((case2, cnt))
    return -1


A, B = map(int, input().split())
print(f(A, B))
