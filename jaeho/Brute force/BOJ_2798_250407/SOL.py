import sys
sys.stdin = open('input.txt','r')
#########################################

card_gaesu,limit=map(int,input().split())
card_jongru=list(map(int,input().split()))
stack=[]
for i in range(card_gaesu):
    for j in range(i+1,card_gaesu):
        for k in range(j+1,card_gaesu):
            if card_jongru[i]+card_jongru[j]+card_jongru[k] <=limit:
                stack.append(card_jongru[i]+card_jongru[j]+card_jongru[k])
print(max(stack))