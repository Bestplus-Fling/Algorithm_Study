import sys
sys.stdin = open('input.txt', 'r')
######################################


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

garage = [0] * (arr[-1][0] + 1)

for info in arr:
    garage[info[0]] = info[1]

changed = arr[0][0]
height = arr[0][1]

max_changed = arr[0][0]
max_height = arr[0][1]

for i in range(changed, len(garage)):
    # 0인경우엔 continue
    if not garage[i]: continue
    if height < garage[i]:
        if garage[i] > max_height:
            # 본인 이전까지 갱신
            for j in range(max_changed, i):
                garage[j] = max_height
            changed = i + 1
            max_height = garage[i]
            max_changed = i + 1

            height = garage[i]
        else:
            for j in range(max_changed, i):
                if garage[j] > garage[i]: continue
                garage[j] = garage[i]
            changed = i + 1
            height = garage[i]
    # 높이가 같은 경우엔 changed와 max_changed를 갱신하고 높이를 확정지음
    elif height == garage[i]:
        for j in range(changed, i):
            garage[j] = garage[i]
        changed = i + 1
        if garage[i] == max_height:
            max_changed = changed

    else:
        for j in range(changed, i):
            garage[j] = garage[i]
        changed = i + 1
        height = garage[i]
    # print(i, garage)

print(sum(garage))