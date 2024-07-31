# 도움 받은 풀이
def solution(s):
    answer = -1

    stack = []
    
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()  # 짝을 이루는 문자 제거
        else:
            stack.append(i)
            
    if stack:
        answer = 0
    else:
        answer = 1

    return answer
