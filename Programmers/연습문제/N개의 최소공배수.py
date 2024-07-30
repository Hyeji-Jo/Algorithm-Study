def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(arr):
    from collections import deque
    dq = deque(arr)
    answer = 0
    
    if len(arr) < 2:
        return arr[0]
    else:
        while len(dq) > 1:
            x = dq.pop()
            y = dq.popleft()
            multi = (x*y) // gcd(y, x)
            dq.appendleft(multi)

    return dq[0]

# 코드 경량화
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(arr):
    
    if len(arr) < 2:
        return arr[0]
    else:
        answer = arr[0]
        
        for num in arr[1:]:
            answer = (answer*num)//gcd(answer,num)

    return answer


# 다른 사람의 풀이
from fractions import gcd


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer
