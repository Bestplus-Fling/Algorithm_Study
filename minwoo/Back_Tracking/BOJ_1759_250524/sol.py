import sys
sys.stdin = open('input.txt', 'r')

# 서로 다른 L개의 알파벳(dfs) 소문자들로 구성
"""
최소 한 개의 모음(a, e, i, o, u가 있는 배열)과 최소 두 개의 자음으로 구성
또한 정렬된 문자를 선호 -> 알파벳이 증가하는 순서로 배열되었을 것이라고 추측
C개의 문자들이 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램
"""
vowel = {'a', 'e', 'i', 'o', 'u'}


def dfs(depth, idx, word, check, valid):
    global alphabet, L, C, answer
    # 검증하는데 오래 걸리면 안될듯
    # 그러니까 dfs 인자로 배열을 하나 생성
    # [0]은 모음 여부를 확인, 한번이라도 들어갔다면 1
    # [1]은 자음 여부, 2를 넘기지 못하면 그대로 리턴
    if depth == L:
        # 검증하는 함수 필요
        if valid[0] > 0 and valid[1] > 1:
            answer.add(word)
        return
    for c in range(idx, C):
        if check[c] == 1:
            continue
        FLAG = False
        check[c] = 1
        if (a := alphabet[c]) in vowel:
            valid[0] += 1
            FLAG = True
        else:
            valid[1] += 1
        dfs(depth+1, c+1, word+a, check, valid)
        valid[(0 if FLAG else 1)] -= 1
        check[c] = 0


L, C = map(int, input().split())
alphabet = sorted(list(input().strip().split()))
# print(alphabet)
answer = set()
dfs(0, 0, '', [0]*C, [0]*2)
print(*sorted(list(answer)), sep='\n')
