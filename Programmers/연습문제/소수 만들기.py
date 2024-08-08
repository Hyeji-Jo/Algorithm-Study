import itertools

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def solution(nums):
    answer = 0
    nums_lst = list(itertools.combinations(nums, 3))
    
    for i in nums_lst:
        num = sum(i)
        if count_divisors(num) == 2:
            answer +=1

    return answer

# 다른 사람의 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
