def solution(t, p):
    answer = 0
    a = len(p)
    
    for i in range(len(t)-a+1):
        target = int(t[i:i+a])
        if target <= int(p):
            answer += 1

        
    return answer

# 다른 사람의 풀이
def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer
