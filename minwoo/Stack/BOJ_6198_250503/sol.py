import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# 1. 완탐
# 한칸 한칸 다 보면서 마지막 top값보다 작은 값을 만나면 중단
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# ans = 0
# for i in range(N):
#     stack = []
#     cnt = 0
#     for j in range(i+1, N):
#         # [i] 와 크거나 같은 경우 종료
#         if arr[i] <= arr[j]:
#             break
#         stack.append(arr[j])
#         cnt += 1
#     ans += cnt

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = 0
# 2. 스택 최적화
# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있다면, 그 다음 옥상은 보지 못한다.
# 스택삽입
# top보다 높이가 높은 경우
stack = []
cnt = 0
for h in arr:
    while stack:
        if stack[-1] <= h:
            stack.pop()
            cnt -= 1
        else:
            break
    ans += cnt
    stack.append(h)
    cnt += 1

print(ans)
