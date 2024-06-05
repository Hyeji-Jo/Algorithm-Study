def solution(my_string, is_prefix):
    answer = 0
    
    lst = []
    for i in range(len(my_string)):
        if is_prefix == my_string[:i+1]:
            answer += 1

        
    return answer

# 다른 사람 코드
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
