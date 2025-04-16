import sys
sys.stdin = open("input.txt", "r")


def value_max(cube, out_num):
    val_max = 0
    for ii in range(6):
        if ii in out_num:
            continue
        val_max = max(val_max, cube[ii])
    return val_max


N = int(input())
cubes = [list(map(int, input().split())) for _ in range(N)]
check = [5, 3, 4, 1, 2, 0]
result = 0
for i in range(6):
    before_num = cubes[0][i]
    value = value_max(cubes[0], [i, check[i]])
    for j in range(1, N):
        t = cubes[j].index(before_num)
        value += value_max(cubes[j], [t, check[t]])
        before_num = cubes[j][check[t]]
    result = max(result, value)
print(result)