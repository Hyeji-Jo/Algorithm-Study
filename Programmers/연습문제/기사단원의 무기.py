# 시간 초과 발생
def solution(number, limit, power):
    answer = 0
    lst = []
    
    # 약수의 수 count
    for i in range(1, number + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count > limit:
            lst.append(power)
        else:
            lst.append(count)
    
    answer = sum(lst)

# 도움 받은 풀이
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def solution(number, limit, power):
    total_weight = 0
    
    for i in range(1, number + 1):
        divisor_count = count_divisors(i)
        if divisor_count > limit:
            total_weight += power
        else:
            total_weight += divisor_count
    
    return total_weight
