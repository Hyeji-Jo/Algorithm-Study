# 시간 초과 풀이
import itertools
def solution(n):
    answer = 0
    combi = []
    a = [1,2]
    
    for i in range(1, n+1):
        combi += list(itertools.product(a,repeat=i))
        
    for com in combi:
        if sum(com) == n:
            answer += 1
    
    
    return answer

# 도움 받은 풀이
def solution(n):
    answer = 0
    fib = [1]*(n+1)
    
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    
    
    return fib[n]%1234567
