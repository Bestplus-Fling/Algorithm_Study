import sys
sys.stdin = open("input.txt", "r")


def back(depth, num_list, check):
    global in_case

    if depth == M:
        if (num_join := ' '.join(num_list)) not in in_case:
            in_case.add(num_join)
        return

    for i in range(1, N+1):
        if check[i]: continue
        back(depth+1, num_list+[str(i)], check)


N, M = map(int, input().split())
in_case = set()
back(0, [], [0] * (N+1))
print('\n'.join(sorted(list(in_case))))
