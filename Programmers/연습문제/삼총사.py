def solution(number):
    import itertools
    answer = 0
    combie = list(itertools.combinations(number,3))
    for i in combie:
        if sum(i) == 0:
            answer += 1
    return answer
