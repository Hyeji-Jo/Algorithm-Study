from itertools import product
def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        for per in product(li,repeat = i):
            answer.append(''.join(per))
    answer.sort()
    return answer.index(word)+1

# 다른 사람의 풀이
def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        if w not in ans: ans.append(w)
    ans.sort()
    answer = ans.index(word)
    return answer
