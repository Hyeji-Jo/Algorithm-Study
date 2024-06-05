def solution(n, control):
    
    w_cnt = control.count('w')
    s_cnt = control.count('s')
    d_cnt = control.count('d')
    a_cnt = control.count('a')
    
    answer = n + w_cnt - s_cnt + (10*d_cnt) - (10*a_cnt)
    return answer

# 다른 사람 코드
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer
