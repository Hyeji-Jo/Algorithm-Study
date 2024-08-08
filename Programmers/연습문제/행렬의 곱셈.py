import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    new1 = np.array(arr1)
    new2 = np.array(arr2)
    answer = np.dot(new1, new2).tolist()
    return answer
