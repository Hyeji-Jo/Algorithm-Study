def solution(price, money, count):
    answer = -1
    
    need = 0
    for i in range(1, count+1):
        need += (price*i)

    answer = need-money
    if answer < 0:
        return 0
    else: 
        return answer


# 다른 사람의 풀이
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
