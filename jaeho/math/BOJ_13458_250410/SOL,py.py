import sys
sys.stdin = open('input.txt','r')
#########################################

test_room_gaesu=int(input())
one_room_student=list(map(int,input().split()))
real_gamdok_see,bu_gamdok=map(int,input().split())

stack=[]
#결과값은 방개수+@
result=test_room_gaesu
#방개수만큼순회
for i in range(test_room_gaesu):
    #스택 값에 한방당 학생수 -본감독관 볼수있는 인원
    stack.append(one_room_student[i]-real_gamdok_see)
    # 만약 스택 값이 테스트 방개수와 같으면
    if len(stack)==test_room_gaesu:
        #스택에 쌓인걸 순회
        for namun_student in stack:
            #만약 남은학생이 영보다 작으면 넘어가라
            if namun_student <= 0:
                continue
                # 남은 학생이 부감독 보다 작으면 플러스1
            elif namun_student<bu_gamdok:
                result+=1
            # 만약 같으면 +1
                #만약 부감독 보다 큰면
            elif namun_student>=bu_gamdok:
                #부감독으로 나누어지면
                if namun_student%bu_gamdok==0: ###여기틀림 2가 아니라 남은 감독 인원으로 나누어 떨어지는지 확인해야됨
                    #j값에서 부감독 나눈값 더하기
                    result+=namun_student//bu_gamdok
                    #부감독으로 안나누어지면
                else:
                    result+=namun_student//bu_gamdok+1

print(result)