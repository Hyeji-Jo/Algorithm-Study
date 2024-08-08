# 도움 받은 코드
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache_que = deque(maxlen=cacheSize)
    
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        if city in cache_que:
            cache_que.remove(city)
            cache_que.append(city)
            answer += 1
        else:
            if len(cache_que) >= cacheSize:
                cache_que.popleft()
            cache_que.append(city)
            answer += 5

    return answer
