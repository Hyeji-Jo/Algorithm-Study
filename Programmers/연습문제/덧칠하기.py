# 도움 받은 코드
def solution(n, m, section):
    answer = 0
    painted = 0
    
    for s in section:
        if s > painted:
            answer += 1
            painted = s+m-1
    
    return answer

# 다른 사람의 풀이
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer
