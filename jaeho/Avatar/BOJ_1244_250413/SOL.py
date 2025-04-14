import sys
sys.stdin = open('input.txt','r')
#########################################

switch_len=int(input())
switch_status=list(map(int,input().split()))
student_number=int(input())
for i in range(student_number):
    jender,start_switch=map(int,input().split())

    #1based 인덱스를 0 based 로 변환
    start_idx= start_switch-1

    # 만약 남자라면
    if jender == 1:
        # 시작 스위치 인덱스-1 에서 스위치 길이만큼 스타트 스위치 배수만큼 건너뛰기
        for i in range(start_idx,switch_len,start_switch):
            #스위치 상태는 1을 0으로 0을 1로
            switch_status[i] = 1-switch_status[i]
    # 여자라면
    else:
        #대칭 아니면 자기 꺼만 바꿈 자기 위치니는 시작위치 -1
        switch_status[start_idx] = 1 - switch_status[start_idx]
        #1 부터 스위치 길이만큼 순회(왼쪽 오른쪽 기준 정하기)
        for j in range(1,switch_len):
            #왼쪽은 시작위치에서 -1
            left=start_idx - j
            #오른쪽은 시작위치에서 +1
            right=start_idx + j
            # 범위 넘어가면 종료
            if left<0 or right >= switch_len:
                break
            # 자기가 받은수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장
            if switch_status[left] == switch_status[right]:
                # 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치상태 바꿈
                switch_status[left] = 1 - switch_status[left]
                switch_status[right] = 1 - switch_status[right]
            #아니면 끝내라
            else:
                break


cnt=0
#스위치 상태 순회
for status in switch_status:
    # 띄어서 출력
    print(status, end= ' ')
    # 카운트 셈
    cnt+=1
    #만약 20으로 나누어 떨어지면
    if cnt%20==0:
        #줄 나눠서 출력
        print()


