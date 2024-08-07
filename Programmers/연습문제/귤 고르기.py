# 시간 초과 풀이
def solution(k, tangerine):
    answer = 0
    count_lst = []
    
    for i in range(1, max(tangerine)+1):
        count_lst.append(tangerine.count(i))
    
    count_lst.sort(reverse=True)
    
    for i in count_lst:
        answer+=1
        k-=i
        if k <= 0:
            break
    
    return answer

# 도움 받은 풀이
from collections import Counter
def solution(k, tangerine):
    answer = 0
    size_count = Counter(tangerine)
    count_list = sorted(size_count.values(), reverse=True)
    
    for i in count_list:
        answer+=1
        k-=i
        if k <= 0:
            break
    
    return answer
