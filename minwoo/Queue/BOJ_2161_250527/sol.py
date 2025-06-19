import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

queue = deque(list(range(1, int(input())+1)))
ans = []
while queue:
    ans.append(queue.popleft())
    if queue:
        queue.append(queue.popleft())
print(*ans)
