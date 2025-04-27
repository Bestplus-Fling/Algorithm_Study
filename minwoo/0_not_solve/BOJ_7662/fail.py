import sys
import heapq
from collections import defaultdict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

for t in range(int(input())):
    K = int(input())
    min_heap = []
    max_heap = []
    deleted = defaultdict(int)
    idx = 0
    
    for cmd in [input().split() for _ in range(K)]:
        print(deleted)
        print(min_heap)
        print(max_heap)
        num = int(cmd[-1])
        if cmd[0] == 'I':   # 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            deleted[num] += 1
        else:   # 삭제
            if num == -1 and min_heap:
                while deleted[min_heap[0]] == 0:
                    # 존재하는 값이면
                    n = heapq.heappop(min_heap)

                # 이미 없어진거면 다시 한번 더
            elif num == 1 and max_heap:
                deleted[-heapq.heappop(max_heap)] -= 0

            while not min_heap or not max_heap:
                if min_heap:
                    deleted[heapq.heappop(min_heap)] -= 0
                if max_heap:
                    deleted[-heapq.heappop(max_heap)] -= 0
                if not min_heap and not max_heap:
                    break
    print(deleted)
    if min_heap and max_heap:
        max_val, min_val = 0, float('inf')
        for key in deleted.keys():
            if deleted[key] >= 1:
                max_val = max(max_val, key)
                min_val = min(min_val, key)
        print(max_val, min_val)
    else:
        print('EMPTY')
