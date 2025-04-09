import sys
sys.stdin = open('input.txt', 'r')
#########################################

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())


'''
시작위치에서 t 만큼 움직였을 때
12 나누기 6의 몫은 몇번 튕겼는지 알려주는거
p + t % w는 얘가 튕기고 나서도 몇칸 움직였는지 알려주는거
무조건 정방향으로 이동하니까 몫이 홀수
너비의 끝에서 몇칸 이동했는지 
짝수면 0에서 몇칸 움직였나
'''


if (p + t) // w % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if (q + t) // h % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h


print(x, y)



