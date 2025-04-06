Round=int(input())
#a 리스트
a_list=[]
#b 리스트
b_list=[]

for _ in range(Round):
    #a카드 받아오고
    a_card=list(map(int,input().split()))
  #개수는  필요 없으니 날리고 
    a_card.pop(0)
  #a리스트에 넣기
    a_list.append(a_card)
    #b카드 받아오고
    b_card=list(map(int,input().split()))
 #개수는  필요 없으니 날리고 
    b_card.pop(0)
    #b리스트에 넣고
    b_list.append(b_card)
#라운드만큼 순회
for i in range(Round):
    if a_list[i].count(4) > b_list[i].count(4):
        print("A")
    elif a_list[i].count(4) < b_list[i].count(4):
        print("B")
    elif a_list[i].count(4) == b_list[i].count(4):
        if a_list[i].count(3) > b_list[i].count(3):
            print("A")
        elif a_list[i].count(3) < b_list[i].count(3):
            print("B")
        elif a_list[i].count(3) == b_list[i].count(3):
            if a_list[i].count(2) > b_list[i].count(2):
                print("A")
            elif a_list[i].count(2) < b_list[i].count(2):
                print("B")
            elif a_list[i].count(2) == b_list[i].count(2):
                if a_list[i].count(1) > b_list[i].count(1):
                    print("A")
                elif a_list[i].count(1) < b_list[i].count(1):
                    print("B")
                elif a_list[i].count(1) == b_list[i].count(1):
                    print("D")