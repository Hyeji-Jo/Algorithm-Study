def solution(numbers):
    import itertools
    answer = []
    lst = list(itertools.combinations(numbers,2))
    
    for i in lst:
        a = sum(i)
        if a not in answer:
            answer.append(a)
            
    return sorted(answer)

# 다른 사람의 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))
