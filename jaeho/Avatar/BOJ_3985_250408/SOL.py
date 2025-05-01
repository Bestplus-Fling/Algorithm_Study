cake_len=int(input())
saram_number=int(input())
arr=[0]*(cake_len+1)
stack=[]
max_1=0
#가장 많은 조각을 받을것을 기대하고 있던 방청객의 번호 (그냥 범위넓은사람 인덱스)
for i in range(1,saram_number+1):
    # 시작과 끝
    start,end=map(int,input().split())
    #만약 끝-시작이 맥스값보다 크면
    if end-start>max_1:
        #최대값은 끝-스타트
        max_1=end-start
        #그리고 해당 인덱스 넣기
        stack.append(i)

        #숫자들을 각자 카운팅
    for j in range(start,end+1):
        if arr[j] == 0:
            arr[j] = i
        else:
            continue
# 가장 많은 조각을 받은 사람의 번호
result=[]
max_2=0
for o in range(1,saram_number+1):
    cnt = 0
    #arr 순회
    for x in arr:
        #만약 x가 o 와같으면
        if x==o:
            #카운트
            cnt+=1
            #만약 카운트가 맥스보다 크면 맥스는 카운트 하고 해당인덱스 리설트 에추가
        if cnt>max_2:
            max_2=cnt
            result=[o]




#가장 많은 조각을 받을것을 기대하고 있던 방청객의 번호 그냥 범위넓은사람 인덱스
print(max(stack))
# 많이받은사람 인덱스
print(*result)