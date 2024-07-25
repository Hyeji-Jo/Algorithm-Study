def solution(s):
    # 중심값 저장
    center = len(s)//2
    
    # 짝수일 경우
    if len(s)%2 ==0:
        answer = s[center-1:center+1]
        
    # 홀수일 경우
    else:
        answer = s[center]
    return answer

# 다른 사람의 풀이
def string_middle(str):
    a = len(str)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return str[int(a) : -int(a)]
