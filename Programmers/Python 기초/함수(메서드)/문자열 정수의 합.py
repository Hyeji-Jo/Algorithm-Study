def solution(num_str):
    answer = 0
    
    for i in num_str:
        answer += int(i)
    return answer


# 다른 사람 풀이
def solution(num_str):
    return sum([int(i) for i in num_str])
