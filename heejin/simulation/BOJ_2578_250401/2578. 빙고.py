import sys
sys.stdin = open("2578.  빙고.txt", "r")

'''
가로 세로 대각선에 해당하는 5개의 모든 수가 지워지는 경우 빙고이다. 사회자가 몇 번째 수를 부른 후 빙고인지 출력

1~5 줄은 빙고판의 쓰여진 수
6~10 줄은 사회자가 부르는 수

5*5에는 1~25까지의 수가 한번씩 사용



'''
n=5
cnt=0
bingo=[list(map(int, input().split())) for _ in range(n)]
answer=[list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        cnt+=1
        call = answer[i][j]

        # 빙고=> 0
        for k in range(n):
            for l in range(n):
                if bingo[k][l] == call:
                    bingo[k][l] = 0

        bingo_cnt=0

        # 가로 세로 체크
        for x in range(n):
            if sum(bingo[x]) == 0:
                bingo_cnt +=1
            if sum(bingo[k][x] for k in range(n)) == 0 :
                bingo_cnt +=1

        # 대각선 체크
        if sum(bingo[a][a] for a in range(n)) == 0 :
            bingo_cnt +=1
        if sum(bingo[a][n - 1 - a] for a in range(n)) == 0:
            bingo_cnt += 1

        if bingo_cnt >= 3:
            print(cnt)
            break
    else:
        continue
    break


