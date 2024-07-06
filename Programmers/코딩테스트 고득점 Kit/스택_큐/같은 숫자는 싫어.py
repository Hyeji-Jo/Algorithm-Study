def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
        else:
            pass
    return answer

# 다른 사람의 풀이
def no_continuous(s):
    # 함수를 완성하세요
    result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result
