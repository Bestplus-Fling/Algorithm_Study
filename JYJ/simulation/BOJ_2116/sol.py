import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
0 : 5
1 : 4
2 : 3

'''

n = int(input())

dice = [list(map(int,input().split())) for _ in range(n)]
updown = {0 : 5, 1 : 3, 2 : 4, 5 : 0, 4 : 2, 3 : 1}
max_cnt = 0
for i in range(6):
    cnt = 0
    a = dice[0][updown[i]]
    for j in range(n):
        max_num = 0
        idx = 0
        for k in range(6):
            if a == dice[j][k]:
                idx = k
                a = dice[j][updown[k]]
                break

        for l in range(6):
            if l == idx or l == updown[idx]:
                continue

            if max_num == 6:
                break

            max_num = max(max_num, dice[j][l])

        cnt += max_num

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)




