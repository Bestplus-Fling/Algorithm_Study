import sys
sys.stdin = open('input.txt', 'r')
#########################################

'''
모든 전구를 끄려고 한다. i 번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전

모든 전구를 끄기 위해서 스위치를 몇 번 눌러야 하는지
'''

# 아웃풋 1 2 0 4

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    jeongu = list(input())
    cnt = 0
    for i in range(1,len(jeongu)+1):
        if jeongu[i-1] == 'Y':
            jeongu[i-1] = 'N'
            cnt += 1
            for j in range(i, len(jeongu)+1):
                if j % i == 0:
                    if jeongu[j-1] == 'N':
                        jeongu[j-1] = "Y"
                    else:
                        jeongu[j-1] = 'N'


    print(cnt)