def solution(num_list):
    answer = 0
    for i in num_list:
        if len(num_list) >= 11 :
            answer += i
        else:
            if answer == 0:
                answer = i
            else :
                answer *= i
    return answer

# 다른 사람의 풀이
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)
