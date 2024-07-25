def solution(arr1, arr2):
    import numpy as np
    answer = [[]]
    
    a = np.array(arr1)
    b = np.array(arr2)
    answer = a+b

    return answer.tolist()

# 다른 사람의 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer
