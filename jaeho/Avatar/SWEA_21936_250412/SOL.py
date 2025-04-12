import sys
sys.stdin = open('input.txt','r')
#########################################

T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    mun_len,beom=map(int,input().split())
    str_=input()
    result=None
    for i in range(mun_len-beom+1):
        str_dap = str_[i:i+beom]
        if str_dap==str_dap[::-1]:
            result=str_dap
            break
    if result:
        print(f"#{tc} {result}")
    else:
        print(f"#{tc} NONE")


