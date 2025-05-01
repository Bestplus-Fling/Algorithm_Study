import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot = [0] * 31
    for i in carrot:
        carrot[i] += 1
    result = float('inf')
    for i in range(31):
        for j in range(i, 31):
            small, middle, big = sum(carrot[:i]), sum(carrot[i:j]), sum(carrot[j:])
            temp = [small, middle, big]
            if 0 in temp:
                continue
            case = max(temp) - min(temp)
            result = min(result, case)
    print(f'#{tc}', result if result != float('inf') else -1)

