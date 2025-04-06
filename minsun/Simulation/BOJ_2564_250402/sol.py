import sys
sys.stdin = open("input.txt", "r")

def find_location(direction, distance):
    d_result = 0
    if direction == 1: # 북
        d_result = distance
    elif direction == 2: # 남
        d_result = width + height + (width-distance)
    elif direction == 3: #서
        d_result = width + height + width + (height - distance)
    elif direction == 4: #남
        d_result = width + distance

    return d_result


width, height = map(int, input().split())
store_count = int(input())
store_info = [list(map(int, input().split())) for _ in range(store_count)]
ddong = list(map(int, input().split()))

total_width = (width*2) + (height*2) # 사각형 길이
ddong_location = find_location(ddong[0], ddong[1]) # 동근이의 위치

result = 0

for i in range(store_count):
    store_location = find_location(store_info[i][0], store_info[i][1]) # 상점의 거리

    ddong_clockwise = abs(ddong_location - store_location) #시계
    ddong_ban_clockwise = total_width - ddong_clockwise #반시계

    result += min(ddong_ban_clockwise, ddong_clockwise)

print(result)