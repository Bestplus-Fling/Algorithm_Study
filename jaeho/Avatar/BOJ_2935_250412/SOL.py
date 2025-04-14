import sys
sys.stdin = open('input.txt','r')
#########################################
arr = [list(input().split()) for _ in range(3)]
num1=(int(*arr[0]))
num2=(int(*arr[2]))
hap_gop=(str(*arr[1]))
if hap_gop == '+':
    print(num1+num2)
elif hap_gop == '*':
    print(num1 * num2)
