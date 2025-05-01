import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
N = 10
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 0
    for num in arr:
        if num % 2 != 0:
            result += num
    print(f'#{tc}', result)
