'''
아래 <그림 1>과 같이 직사각형 모양의 종이가 있다.
이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다.
가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고,
세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지,
세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다. 예를 들어, <그림 1>의 가로 길이 10㎝이고
 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번 가로 점선을 따라 자르면
  <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때,
가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.
'''
import sys
sys.stdin = open('input.txt','r')
#########################################

garo, sero = map(int,input().split())

garo_arr = [0, garo]
sero_arr = [0, sero]

cut_count=int(input())
for _ in range(cut_count):
    ga_se_check, cut = map(int,input().split()) #가로 자르는 건0,세로 자르는건1
    if ga_se_check == 1:
        garo_arr.append(cut)
    else:
        sero_arr.append(cut)

garo_arr.sort()
sero_arr.sort()
ga_hap = 0
for i in range(1,len(garo_arr)):
    ga_hap=max(ga_hap,garo_arr[i]-garo_arr[i-1])
se_hap = 0
for j in range(1, len(sero_arr)):
    se_hap=max(se_hap,sero_arr[j]-sero_arr[j-1])


print(ga_hap*se_hap)