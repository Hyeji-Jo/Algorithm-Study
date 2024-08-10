# 도움 받은 풀이
def is_prime(n):
    """소수 판별 함수"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def devert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
def solution(n, k):
    answer = 0
    if k == 10 :
        n = n
    else:
        n = devert(n,k)
    
    for num in str(n).split('0'):
        if num and is_prime(int(num)):
            answer += 1
    
    return answer
