# 다른 사람의 풀이
def solution(s):
    answer = ''
    a = list(map(int, s.split(' ')))
    return str(min(a)) + ' ' + str(max(a))
