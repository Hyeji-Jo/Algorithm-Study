def solution(my_string, target):
    answer = 1 if target in my_string else 0
    return answer

# 다른 사함 풀이
def solution(my_string, target):
    return int(target in my_string)
