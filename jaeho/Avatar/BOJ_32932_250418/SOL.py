import sys
sys.stdin = open('input.txt','r')
#########################################
#장애물개수,제어 개수
trash_num,control_num=map(int,input().split())
trash_x_y=[list(map(int,input().split())) for _ in range(trash_num)]
    #이동
shift=list(input().strip())
drX_ronY=[0,0] #초기 드론 xy좌표
#명령어 순회
for i in range(control_num):
    #만약 왼쪽 명령어 나오면
    if shift[i] == 'L':
        #초기좌표 x(0인덱스) 부분 -1
        drX_ronY[0]-= 1
        #근데 만약 드론xy 좌표안에 쓰레기 xy
        if drX_ronY in trash_x_y:
            # 초기좌표 x(0인덱스) 부분다시 +1
            drX_ronY[0] += 1
            #넘어가기
            continue

    if shift[i] == "D":
        drX_ronY[1]-= 1
        if drX_ronY in trash_x_y:
            drX_ronY[1] += 1
            continue
    if shift[i] == 'R':
        drX_ronY[0]+= 1
        if drX_ronY in trash_x_y:
            drX_ronY[0] -= 1
            continue
    if shift[i] == 'U':
        drX_ronY[1]+= 1
        if drX_ronY in trash_x_y:
            drX_ronY[1] -= 1
            continue

print(*drX_ronY)

