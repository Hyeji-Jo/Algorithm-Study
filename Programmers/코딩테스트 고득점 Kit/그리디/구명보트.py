# 다른 사람의 풀이 (시간 초과)
def solution(people, limit):
    answer = 0
    lst = sorted(people)
        
    while lst:
        person = lst.pop()
        if len(lst) >0 and person+lst[0] <= limit:
            lst.remove(lst[0])
        
        answer += 1
    return answer

# 다른 사람의 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


def solution(people, limit):
    from collections import deque
    answer = 0
    lst = deque(sorted(people))
        
    while len(lst)>1:
        if lst[0] + lst[-1] > limit:
            lst.pop()
            answer += 1
        else:
            a = lst.pop()
            b = lst.popleft()
            answer += 1
    
    if lst:
        answer += 1
