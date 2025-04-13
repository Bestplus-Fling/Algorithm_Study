import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot_box = [0] * 31
    for i in carrot:
        carrot_box[i] += 1
    result = float('inf')
    for i in range(31):
        for j in range(i, 31):
            small, middle, big = sum(carrot_box[:i]), sum(carrot_box[i:j]), sum(carrot_box[j:])
            temp = [small, middle, big]
            if 0 in temp:
                continue
            case = max(temp) - min(temp)
            result = min(result, case)
    print(f'#{tc}', result if result != float('inf') else -1)

