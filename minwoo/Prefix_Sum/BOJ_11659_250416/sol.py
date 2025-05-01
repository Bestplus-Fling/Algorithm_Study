import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
for i in range(N):
    prefix_sum.append(nums[i] + prefix_sum[i])
for i in range(M):
    r, l = map(int, input().split())
    print(prefix_sum[l] - prefix_sum[r-1])