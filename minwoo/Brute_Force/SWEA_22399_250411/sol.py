def is_valid(s, m, b):
    global result
    if not s or not m or not b:
        return -1
    if s[-1] == m[0] or m[-1] == b[0]:
        return -1
    temp = [len(s), len(m), len(b)]
    value = max(temp) - min(temp)
    if value > result:
        return -1
    return value


def div_carrot():
    global carrot, result
    for i in range(N):
        for j in range(N):
            eds = i
            stm, edm = eds, i + j
            stb = edm
            if 0 == eds or stm == edm or stb == N: continue
            s, m, b = carrot[:eds], carrot[stm:edm], carrot[stb:]
            value = is_valid(s, m, b)
            if value != -1:
                result = min(value, result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = sorted(list(map(int, input().split())))
    result = float('inf')
    div_carrot()
    print(f"#{tc}", result if result != float('inf') else -1)
    # break
    # 대, 중, 소 상자로 구분
    # 같은 크기의 당근은 같은 상자
    # 비어있는 상자 x
    # 각 상자에 든 개수 차이가 최소가 되도록 포장