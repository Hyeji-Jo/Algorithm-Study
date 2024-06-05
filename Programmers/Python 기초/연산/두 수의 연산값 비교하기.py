def solution(a, b):
    
    
    s = int(str(a)+str(b))
    answer = s if s >= (2*a*b) else (2*a*b)
    
    return answer

# 다른 사람 풀이
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
