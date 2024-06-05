def solution(num_list):
    answer = 0
    
    g = 1
    for i in num_list:
        g *= i
    
    if g < sum(num_list)**2:
        answer +=1
    return answer

# 다른 사람 풀이
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0
