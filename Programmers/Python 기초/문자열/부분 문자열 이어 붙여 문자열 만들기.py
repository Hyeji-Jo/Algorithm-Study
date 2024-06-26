def solution(my_strings, parts):
    answer = ''
    for n,i in enumerate(my_strings):
        s,e = parts[n]
        answer += i[s:e+1]
        
    return answer

# 다른 사람의 풀이
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
