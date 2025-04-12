import sys
sys.stdin = open('input.txt', 'r')
#########################################


'''
n개의 당근을 주문하면 대, 중, 소 상자로 구분한다
비어있는 상자가 있으면 안 된다

각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다

한 바구니에 같은 당근 담을거니까 개수 세서 집어넣는다

'''


T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    carrot_size = list(map(int,input().split()))
    pojang = [0] * 31
    result = float('inf')
    for i in range(n):
        pojang[carrot_size[i]] += 1

    # print(pojang)
    count = []
    for i in pojang:
        if i > 0:
            count.append(i)

    # count.sort()
    # print(count)

    for i in range(len(count)):
        for j in range(i, len(count)):
            a = sum(count[:i])
            b = sum(count[i:j])
            c = sum(count[j:])
            if a > 0 and b > 0 and c > 0:
                d = max(a, b, c) - min(a, b, c)
                if d < result:
                    result = d

    if result == float('inf'):
        result = -1

    print(f"#{tc} {result}")
