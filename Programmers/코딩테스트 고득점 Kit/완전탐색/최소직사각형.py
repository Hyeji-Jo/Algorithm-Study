def solution(sizes):
    answer = 0
    a = []
    b = []
    
    for g,s in sizes:
        if g < s:
            l = g
            g = s
            s = l
        else:
            pass
        
        a.append(g)
        b.append(s)
        
    answer = max(a) * max(b)
    return answer

# 다른 사람의 풀이
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
