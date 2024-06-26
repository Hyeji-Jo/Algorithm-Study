def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < ord('l'):
            answer += 'l'
        else:
            answer += i
    return answer


# 다른 사람의 풀이
def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)
