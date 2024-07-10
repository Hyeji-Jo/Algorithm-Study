# 시간 초과 풀이
def solution(prices):
    answer=[]
    
    for i in range(len(prices)):
        count = 0
        for j in prices[i+1:]:
            count += 1
            if j < prices[i]:
                break
        answer.append(count)
    
    return answer

# 다른 사람의 풀이
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer


def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
