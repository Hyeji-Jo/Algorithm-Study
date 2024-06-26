def solution(strArr):
    answer = []
    for n,i in enumerate(strArr):
        if n%2==0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
    return answer

# 다른 사람의 풀이
def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]
