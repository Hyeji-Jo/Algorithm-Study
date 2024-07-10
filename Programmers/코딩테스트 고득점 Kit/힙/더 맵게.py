def solution(scoville, K):
    import heapq
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) > 1:
        new = heapq.heappop(scoville)
        
        if new < K:
            answer += 1
            new +=  (heapq.heappop(scoville)*2)
            heapq.heappush(scoville, new)
        else:
            break
        
    if scoville[0] < K :
        answer = -1
    else:
        pass
            
    
    return answer

# 다른 사람의 풀이
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
