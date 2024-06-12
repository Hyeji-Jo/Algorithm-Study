def solution(strArr):
    answer =[]
    [answer.append(i) for i in strArr if 'ad' not in i]
    return answer

# 다른 사람 풀이
def solution(strArr):
    return [word for word in strArr if 'ad' not in word]
