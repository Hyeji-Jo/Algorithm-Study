def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        answer = my_string.replace(alp, alp.upper())
    else:
        answer = my_string
    return answer

# 다른 사람의 풀이
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())
