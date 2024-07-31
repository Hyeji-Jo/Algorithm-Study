def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ' :
            answer += ' '
            
        else:
            alpha = ord(i)+n

            if i == i.lower():
                if alpha > 122:
                    alpha -= 26
            else:
                if alpha > 90:
                    alpha -= 26

            answer += str(chr(alpha))
    return answer


# 다른 사람의 풀이
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer
