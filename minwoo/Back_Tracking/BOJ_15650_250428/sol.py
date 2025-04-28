import sys
sys.stdin = open("input.txt", "r")


def back(depth, num_list, check):
    global ans, bit
    if depth == M:
        temp = ' '.join(num_list)
        if temp not in ans:
            ans.add(temp)
        return

    for i in range(1, N+1):
        # 비트 확인 => 현재 비트가 있다면 back
        case = int(''.join(['0' if i != N-j else '1' for j in range(N)]), 2)
        if (acc := int(bin(check | case), 2)) in bit:
            continue
        bit.add(acc)
        back(depth+1, num_list + [str(i)], acc)


N, M = map(int, input().split())
ans = set()
bit = set()
back(0, [], 0)
result = sorted(list(ans))
print('\n'.join(result))
