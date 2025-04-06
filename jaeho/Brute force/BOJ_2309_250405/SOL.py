import sys
sys.stdin = open('input.txt','r')
#########################################
#일단 리스트로 다 받아와서 다합산후 7명이니 2명씩뺌
small_man=[int(input())for _ in range(9)]
total= sum(small_man)

#전에 골랐던걸 제끼고 고르는 이중포문
for i in range(9):
    for j in range(i+1,9):
        if total - small_man[i]-small_man[j] == 100:
            # 9명 난쟁이 전부돔
            result=[]
            for k in range(9):
                #만약 선택 된 i,j 부분이 아니라면
                if k!=i and k!=j:
                    result.append(small_man[k])
            result.sort()
            for dap in result:
                print(dap)
            exit()

            #










