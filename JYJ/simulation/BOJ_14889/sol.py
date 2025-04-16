import sys
sys.stdin = open('input.txt', 'r')
#########################################

from itertools import combinations

'''


'''


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
min_num = 999999999999
people = [i for i in range(n)]
for i in combinations(people, n//2):
    # print(i)
    a = list(set(people) - set(i)) # team 1 == i, team 2 == a
    # 모든 사람 people에서 중복제거한 조합 i를 뺸 값 a
    # 팀을 절반 나눈 셈
    start = 0
    link = 0
    for j in range(n//2):
        for k in range(n//2):
            if j == k: continue

            start += arr[i[j]][i[k]]
            link += arr[a[j]][a[k]]

    min_num = min(min_num, abs(start - link))

    if min_num == 0: # 최소가 0이면 계산할 필요 없음
        break
print(min_num)