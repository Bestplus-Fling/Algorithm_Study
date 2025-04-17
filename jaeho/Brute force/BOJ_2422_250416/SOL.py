import sys
sys.stdin = open('input.txt','r')
#########################################
ice_num,notmix_num=map(int,input().split())
#아이스크림 번호리스트
ice_list=list(range(1,ice_num+1))
# 이숫자 들은 드가면 안되요
no_num=set()
for _ in range(notmix_num):
    # 드가면 안되는 숫자
    a, b = map(int, input().split())
    #만들어준 저장소에 튜플로 정렬해서 감싸서 넣기
    no_num.add(tuple(sorted((a,b))))
    # 조합 개수도 중보제거후 넣기
result_stack = set()
for i in range(ice_num):
    for j in range(i+1,ice_num):
        for k in range(j+1,ice_num):
            #3개의 조합들을 구해서 저장소 넣기
            result_stack.add((ice_list[i], ice_list[j], ice_list[k]))

# 저장소에 쌓인 걸 다시 순회 시키는데 만약 순회시킨값 안에 노넘버가가 없으면 +1
cnt=0
for ice_1, ice_2, ice_3 in result_stack:
    # 만약 1,2조합에 노넘버가 없고 1,3 조합에 노넘버가 없고 2,3조합에 노넘버가 없으면  없으면 cnt+=1
    if (tuple(sorted((ice_1, ice_2))) not in no_num and
            tuple(sorted((ice_1, ice_3))) not in no_num and
            tuple(sorted((ice_2, ice_3))) not in no_num):
        cnt += 1

print(cnt)







