import sys
sys.stdin = open('input.txt', 'r')
# 기둥 개수 입력
pillar_count = int(input())
# 높이를 저장할 리스트 (인덱스 = 위치, 값 = 높이)
heights = [0] * 1001
# 가장 높은 기둥의 위치와 높이 추적
max_height = 0
max_pos = 0
# 입력을 받아 heights 배열 채우기
for _ in range(pillar_count):
    pos, height = map(int, input().split())
    heights[pos] = height
    # 값을 받아오는걸 반복하는데 만약 height 값이 최대 height 보다 크면 그값이 최대 높이 그리고 최대높이의 포지션
    if height > max_height:
        max_height = height
        max_pos = pos
#결과합산
result = 0
#왼쪽 계산
left_max = 0

# 왼쪽에서 가장 높은 기둥까지 탐색
for i in range(0, max_pos + 1):
    left_max = max(left_max, heights[i])
    result += left_max

right_max = 0
# 오른쪽에서 가장 높은 기둥까지 역순 탐색
for i in range(1000, max_pos, -1):
    right_max = max(right_max, heights[i])
    result += right_max

# 결과 출력
print(result)
