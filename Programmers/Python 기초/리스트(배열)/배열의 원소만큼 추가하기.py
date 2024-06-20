def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer

# 다른 사람의 풀이
def solution(arr):
    return [i for i in arr for j in range(i)]
