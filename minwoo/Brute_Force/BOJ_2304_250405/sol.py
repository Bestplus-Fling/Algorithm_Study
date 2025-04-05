import sys
sys.stdin = open('input.txt', 'r')


def emutable(start, end, height):
    for q in range(start, end):
        container[q] = height


N = int(input())
data = sorted([tuple(map(int, input().split())) for _ in range(N)])
container = [0] * (data[-1][0] + 1)
print(data)
i = 0
while i < N:
    print(f'현재 면적 : {sum(container)}\n컨테이너 상태{container}')
    # 이미 계산이 완료된 좌표일 경우 continue
    if container[data[i][0]]:
        i += 1
        continue
    max_val, idx = 0, 0
    # 현재 위치 너머에 있는 기둥들의 높이를 확인
    for j in range(i+1, N):
        # 만약 자신보다 높은 기둥을 만났다면
        if data[i][1] < data[j][1]:
            # 기둥의 위치를 저장하고 break
            k = data[j][0]
            break
        # 현재 기둥보다 높은 기둥이 없을 경우에 사용할 최대 높이를 저장
        if max_val < data[j][1]:
            idx = j
            max_val = data[j][1]
    else:   # 정상 종료된 for문의 경우 현재 기둥 이후 중 가장 높은 기둥으로 남은 면적을 채운다.
        if i == N-1:
            emutable(data[i-1][0], data[i][0]+1, data[i][1])
            break
        print(f'현재 기둥{data[i]}, 현재 기둥 제외 가장 큰 기둥{max_val}')
        print(f'구간 너비 {(data[idx][0] - data[i][0]+1)}\n')
        container[data[i][0]] = data[i][1]
        emutable(data[i][0]+1, data[idx][0]+1, max_val)
        # 지금까지 면적을 구한 기둥의 위치까지 continue 할 수 있도록 한다.
        i = idx
        continue
    print(f"구간 너비 {k - data[i][0]}\n")
    emutable(data[i][0], k, data[i][1])
    i += 1
print(container)
print(sum(container))
