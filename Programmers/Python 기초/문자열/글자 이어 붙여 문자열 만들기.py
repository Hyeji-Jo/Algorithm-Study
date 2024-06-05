def solution(my_string, index_list):
    answer = ''
    for i, num in enumerate(index_list):
        answer+=(my_string[num])
    return answer

# 다른 사람 풀이
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])
