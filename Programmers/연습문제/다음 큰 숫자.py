def solution(n):
    answer = 0
    start = n+1
    n_one = bin(n).count('1')
    
    while answer == 0 :
        if bin(start).count('1') == n_one:
            answer += start
            break
        else:
            start += 1
    return answer



# 다른 사람의 풀이
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
