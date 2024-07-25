def solution(s):
    return ''.join(list(reversed(sorted(s))))


# 다른 사람의 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))
