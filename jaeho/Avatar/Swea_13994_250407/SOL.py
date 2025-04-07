import sys
sys.stdin = open('input.txt','r')
#########################################
'''




'''

T = int(input())    # test_case 개수를 받아옴
for tc in range(1, T+1) :
    bus_noseon_check = [0] * 10001
    bus_noseon_gaesu=int(input())
    for _ in range(bus_noseon_gaesu):
        bus_jong,start,end=map(int,input().split())
        for i in range(start,end+1):

            # 일반버스면 구간 모든곳 카운트 체크
            if bus_jong == 1:
                bus_noseon_check[i]+=1
        #급행버스는 start가 짝수인경우 A~B 사이의 모든 짝수번호 정류장에서+1
            #홀수인경우 a,b 사이의 모든 홀수 번호 정류장에 정차
            elif bus_jong == 2:
                if start%2==0 and i%2==0:
                    bus_noseon_check[i]+= 1

                elif start%2==1 and i%2==1:
                    bus_noseon_check[i]+= 1
       # 광역 급행 버스는 A가 짝수인 경우 A와B사이의 모든 4의 배수 번호 정류장에 A가 홀수인  A,B 사이의 3의배수 이면서
            #10의 배수가 아닌 번호
            elif bus_jong == 3:
                if start % 2 == 0 and i % 4 == 0:
                    bus_noseon_check[i] += 1

                elif start % 2 ==1 and i%3 == 0 and i%10 != 0:
                    bus_noseon_check[i] += 1

    print(f"#{tc} {max(bus_noseon_check)}")