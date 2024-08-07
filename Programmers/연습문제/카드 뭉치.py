from collections import deque

def solution(cards1, cards2, goal):
    deq1 = deque(cards1)
    deq2 = deque(cards2)
    answer = 'Yes'
    
    for i in goal:
        if i in deq1 and i==deq1[0]:
            word = deq1.popleft()
        elif i in deq2 and i==deq2[0]:
            word = deq2.popleft()
        else:
            return 'No'
            break
    
    return answer


# 코드 간략히
from collections import deque

def solution(cards1, cards2, goal):
    deq1 = deque(cards1)
    deq2 = deque(cards2)
    
    for word in goal:
        if deq1 and deq1[0] == word:
            deq1.popleft()
        elif deq2 and deq2[0] == word:
            deq2.popleft()
        else:
            return 'No'
    
    return 'Yes'
