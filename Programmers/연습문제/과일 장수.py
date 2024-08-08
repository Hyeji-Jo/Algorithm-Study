def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for num, i in enumerate(score):
        if (num+1) % m == 0:
            answer += i*m
    return answer
