import sys
sys.stdin = open('input.txt','r')
#########################################
#첫째줄에는 해빈이가 아무 차도 부수지 않으면 주차할수있는 공간의 개수
#두번째줄에는 해빈이가 한대를부수고 주차할수있는 공간의 개수
#세번째줄에는 해빈이가 두대를부수고 주차할수있는 공간의 개수
#네번째줄에는 해빈이가 세대를 부수고주차할수있는 공간의 개수
#다섯번째줄에는 해빈이가 네대를 부수고 주차할수있는 공간의 개수

#차의 크기는 2행 2열

# 주차된 차는 X


row,col = map(int,input().split())
Parking_lot =[input() for _ in range(row)]

#[0대 부수고 1대 ,2대 ,3대 ,4대 ]
result=[0]*5

for i in range(row-1):
    for j in range(col-1):
        #몬스터 카 사이즈 2행 이열이니까 정의 함
        Car_size = [Parking_lot[i][j],Parking_lot[i][j+1],Parking_lot[i+1][j],Parking_lot[i+1][j+1]]
        # 존 안에 건물 있으면 넘어감
        if '#' in Car_size:
            continue
            # 다른 자동차 카운트 =존 안에 x를 카운트 차개수를  카운트함
        Other_car_count = Car_size.count('X')
          # 만약에  존안에 X가 3개 나왔다는건 존을 3개 를 부숴야 된다는거니  인덱스 3 번자리 카운트 3 이런식으로
        result[Other_car_count] += 1
#리스트에 담긴거 포문으로 출력
for Output in result:
    print(Output)

