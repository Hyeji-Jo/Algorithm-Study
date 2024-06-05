def solution(start, end_num):
    answer = []
    
    for i in range(start, end_num-1, -1):
        answer.append(i)
    
    return answer


# 다른 사람 코드

def solution(start, end):
    return list(range(start,end-1,-1))
