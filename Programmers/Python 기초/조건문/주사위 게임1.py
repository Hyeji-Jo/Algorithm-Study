def solution(a, b):
    if (a*b)%2 !=0 and (a+b)%2 == 0:
        answer = (a**2) + (b**2)
    elif (a*b)%2 ==0 and (a+b)%2 != 0:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer


# 다른 사함의 풀이
def solution(a, b):
    if a%2 and b%2: return a*a+b*b
    elif a%2 or b%2: return 2*(a+b)
    return abs(a-b)
