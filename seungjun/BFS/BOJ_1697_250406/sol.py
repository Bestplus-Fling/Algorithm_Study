import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
length = 1000000
hide = [False] * length
queue = deque()
hide[n] = True
cnt = 0
queue.append((n, cnt))

while queue:
    now, cnt = queue.popleft()
    if now == k:
        break

    if 0 <= now - 1 < length and not hide[now - 1]:
        hide[now - 1] = True
        queue.append((now - 1, cnt + 1))

    if 0 <= now + 1 < length and not hide[now + 1]:
        hide[now + 1] = True
        queue.append((now + 1, cnt + 1))

    if 0 <= now * 2 < length and not hide[now * 2]:
        if hide[now * 2]: continue
        hide[now * 2] = True
        queue.append((now * 2, cnt + 1))

print(cnt)