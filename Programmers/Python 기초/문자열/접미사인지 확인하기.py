def solution(my_string, is_suffix):
    answer = int(my_string.endswith(is_suffix))
    
    return answer

# 다른 사람 코드

def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)
