# 다른 사람의 풀이
def solution(operations):
    import heapq
    answer = []
    que = []
    
    for i in operations:
        a, num = i.split()
        num = int(num)
        
        if a =='I':
            heapq.heappush(que, num)
        elif a =='D' and len(que) != 0:
            if num ==1 :
                max_num = max(que)
                que.remove(max_num)
            else:
                heapq.heappop(que)

    if len(que) == 0:
        answer = [0,0]
    else:
        answer = [max(que), heapq.heappop(que)]
                
    
    return answer
