def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        lst = []
        for j in range(1, i+1):
            if (j not in lst) and (i%j == 0):
                lst.append(j)
                lst.append(i//j)

        if len(set(lst)) % 2 == 0:
            answer+= i
        else:
            answer -= i
        
    return answer

# 다른 사람의 풀이
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        # 제곱근 값이 정수형으로 나타난 값과 동일한 경우 약수의 갯수는 홀수
        if int(sqrt) == sqrt: #int(i**0.5) == i**0.5
            answer -= i
        # 그 외의 경우에는 짝수
        else:
            answer += i

    return answer
