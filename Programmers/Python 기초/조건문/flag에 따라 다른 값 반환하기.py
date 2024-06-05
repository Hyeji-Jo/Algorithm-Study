def solution(a, b, flag):
    answer = 0
    
    if flag:
        answer = a+b
    else:
        answer = a-b
    
    return answer

# 다른 사람 코드
def solution(a, b, flag):
    if flag: return a+b
    return a-b
