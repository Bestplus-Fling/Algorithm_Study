import sys
sys.stdin = open("input.txt", "r")

# 1: 동쪽, 2: 서쪽, 3: 남쪽, 4: 북쪽
# 같은 변 두번 나온 숫자에서 작은 면적을 확인, 뺀다
N = 6
K = int(input())
rectangle = [[] for _ in range(5)]
for _ in range(N):
    a, _len = map(int, input().split())
    rectangle[a].append(_len)

width_args, corner = [], []
for i in range(1, 5):
    rectangle[i].sort(reverse=True)
    if len(rectangle[i]) == 1:
        width_args.append(rectangle[i][0])
    else:
        corner.append(rectangle[i][1])

print(((width_args[0] * width_args[1]) - (corner[0] * corner[1]))*K)








