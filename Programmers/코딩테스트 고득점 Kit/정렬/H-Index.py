def solution(citations):
    answer = 0
    citations.sort()
    
    for n,i in enumerate(citations):
        if i >= len(citations) - n:
            return len(citations) - n

    return 0

# 다른 사람의 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
