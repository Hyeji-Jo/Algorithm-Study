def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if i % k == 0:
            answer.append(i)
    return answer

# 다른 사람 코드
def solution(n, k):
    return [i for i in range(k,n+1,k)]
