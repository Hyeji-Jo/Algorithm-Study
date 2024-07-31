def solution(s):
    answer = []
    alpha = []
    
    for i in s:
        if i not in alpha:
            answer.append(-1)
            alpha.append(i)
        else:
            answer.append(list(reversed(alpha)).index(i)+1)
            alpha.append(i)
    
    return answer


# 다른 사람의 풀이
def solution(s):
    last_seen = {}  # 각 문자의 마지막 출현 위치를 저장할 딕셔너리
    result = []  # 결과를 저장할 리스트

    for i, char in enumerate(s):
        if char in last_seen:
            result.append(i - last_seen[char])
        else:
            result.append(-1)
        last_seen[char] = i  # 현재 문자의 마지막 출현 위치 업데이트

    return result
