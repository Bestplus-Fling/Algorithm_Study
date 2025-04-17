import sys
sys.stdin = open('input.txt','r')
#########################################

alphabet = 'abcdefghijklmnopqrstuvwxyz'
amho = input().strip()
n = int(input())
dictionary = [input().strip() for _ in range(n)]

#알파벳 길이만큼 반복해야죠
for shift in range(26):
    new_word = ''
    for amhos in amho:
        # 암호는 알파벳 기준 몇번째 인가 그걸로 인덱스로 바꾸기
        index = alphabet.index(amhos)
        # 순환값은 현재값-변화량 나누기 전체수 복호화 의경우 왼쪽으로
        # 가기 때문에 -하고 암호화의 경우 +임
        new_index = (index - shift) % 26
        # 새 문자 이어 붙이기
        new_word += alphabet[new_index]

    # 사전 단어 포함 여부 확인
        # 단어들 출력
    for word in dictionary:
        #만약 단어 안에 새문자가 있으면 그건 정답 출력후 프로그램 끝냄
        if word in new_word:
            print(new_word)
            exit()
