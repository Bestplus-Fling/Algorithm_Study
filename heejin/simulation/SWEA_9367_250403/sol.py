import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  N = int(input())
  C = list(map(int, input().split()))
  max_cnt=1
  cnt=1

  for i in range(N - 1):
      if C[i] < C[i + 1]:
          cnt+= 1
          max_cnt = max(max_cnt, cnt)
      else:
          cnt= 1

  print(f"#{test_case} {max_cnt}")