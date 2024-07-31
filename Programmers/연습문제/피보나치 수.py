# 런타임 에러
def fibo(n):
    if n>=2:
        return fibo(n-1)+fibo(n-2)
    else:
        return n

def solution(n):
    answer = fibo(n)%1234567
    return answer

# 다른 풀이
def solution(n):
    # 피보나치 수를 저장할 리스트 초기화
    fib = [0]*(n+1)
    fib[1] = 1
    
    # 피보나치 수 계산
    for i in range(2, n+1):
        fib[i] = (fib[i-1] + fib[i-2])
        
    answer = fib[n]%1234567
    
    return answer
