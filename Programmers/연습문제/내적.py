def solution(a, b):
    answer = 0
    
    def ne(x,y):
        return x*y
        
    return sum(list(map(ne, a, b)))

# 다른 사람의 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
