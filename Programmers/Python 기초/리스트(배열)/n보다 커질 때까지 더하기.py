def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            break
        else:
            pass
    return answer

# 다른 사람의 풀이
def solution(numbers, n):
    answer = 0
    i=0
    while answer<=n:
        answer+=numbers[i]
        i+=1
    return answer
