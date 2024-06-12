def solution(arr, k):
    answer = []
    for i in arr:
        if k %2 == 0:
            answer.append(i+k)
        else:
            answer.append(i*k)
    return answer

# 다른 사함의 풀이
def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]
