import sys
sys.stdin = open('input.txt','r')
#########################################


T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())  # 숫자의 개수
    arr = list(map(int, input().split()))  # 숫자 리스트 입력

    # 최대값과 최소값 구하기
    max_val = max(arr)
    min_val = min(arr)

    # 조건에 맞는 위치 찾기
    max_pos = len(arr) - 1 - arr[::-1].index(max_val) + 1  # 마지막 등장 → 역순 + 1
    min_pos = arr.index(min_val) + 1  # 첫 번째 등장 + 1

    result = abs(max_pos - min_pos)

    print(f"#{tc} {result}")
