import sys
sys.stdin = open('input.txt', 'r')
######################################
import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())

if s == g:
    can_go = 0
else:
    can_go = 'use the stairs'
    # 1 base
    building = [0] * (f + 1)
    push_dutton = deque()
    push_cnt = 0
    duttons = [u, -d]
    building[s] = float('inf')
    push_dutton.append((s, push_cnt))

    while push_dutton:
        floor, push = push_dutton.popleft()

        push += 1
        for dutton in duttons:
            next_floor = floor + dutton
            if 0 < next_floor <= f:

                if building[next_floor]: continue
                if next_floor == g:
                    can_go = push
                    push_dutton = deque()
                    break
                building[next_floor] = push
                push_dutton.append((next_floor, push))

print(can_go)