def solution(arr, n):
    answer = []
    for i, k in enumerate(arr):
        if len(arr) %2 != 0 and i%2 ==0:
            arr[i] = k+n
        elif len(arr) %2 == 0 and i%2 !=0:
            arr[i] = k+n
        
    return arr


# 다른 사람 풀이
def solution(arr, n):
    if len(arr) % 2:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n

    return arr
