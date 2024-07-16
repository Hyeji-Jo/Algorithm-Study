# 다른 사람의 풀이
def solution(people, limit):
    answer = 0
    lst = sorted(people)
        
    while lst:
        person = lst.pop()
        if len(lst) >0 and person+lst[0] <= limit:
            lst.remove(lst[0])
        
        answer += 1
                
            
    return answer
