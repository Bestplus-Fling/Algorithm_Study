import sys
sys.stdin = open('input.txt', 'r')
#########################################
# 첫 번째 양의 정수
# 두 번째 양의 정수 중 하나 선택
# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다
# 예를 들어 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다

def minus(num1):
    max_cnt = 0
    my_list1 = []
    for i in range(1, num1 + 1):
        hund = num1
        numi = i
        cnt = 2
        my_list = [num1]
        my_list.append(i)
        while True:
            numbers = hund - numi # i에서 넘버스를 빼야함 그러고 나온 값을 또 저장해야 함
            # 38      100    62
            # 24      62     38
            #         38     24
            hund = numi
            numi = numbers  # 저장한 값을 넘버스에서 빼줘야 함

            if numbers < 0:
                break
            my_list.append(numbers) # 출력을 하기 위해 리스트에 100하고 62도 추가해야 함 중복 x
            # 38 24 >> 38 이후부터는 numbers 밖에 안들어감
            # 뺄 때마다 카운팅
            cnt += 1
            # 카운팅의 최댓값 갱신을 해야지
            # numbers의 값이 0보다 작다면 break

        if max_cnt < cnt:
            max_cnt = cnt
            # 그러고 최댓값과 그 숫자(리스트) 출력
            my_list1 = my_list.copy()


    return max_cnt, my_list1



N = int(input())
re, sult = minus(N)

print(re)
print(*sult)







