import sys
sys.stdin = open('input.txt', 'r')


def back(depth, selected, score):
    global result
    if depth == 11:
        # score 의 값이 result보다 크다면 갱신
        result = max(result, score)
        return
    for i in range(N):
        if (acc := data[depth][i]) == 0 or selected[i]:
            continue
        selected[i] = 1
        back(depth+1, selected, score+acc)
        selected[i] = 0


N = 11
C = int(input())
for c in range(C):
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(*data, sep='\n')
    result = 0
    back(0, [0] * N, 0)
    print(result)
