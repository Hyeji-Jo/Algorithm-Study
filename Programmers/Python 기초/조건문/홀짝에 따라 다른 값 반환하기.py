def solution(n):
    a = []
    for i in range(n+1):
        if i % 2 == 0 and n % 2 == 0:
            a.append(i**2)
        elif i % 2 != 0 and n % 2 != 0:
            a.append(i)

    return sum(a)

# 다른 사람 풀이
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
