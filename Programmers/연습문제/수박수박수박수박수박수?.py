def solution(n):
    lst = '수박'*n
    answer = lst[:n]
    return answer

# 다른 사람의 풀이
def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)
