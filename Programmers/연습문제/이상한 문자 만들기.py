def solution(s):
    answer = []
    words = s.split(' ')
    
    for i in words:
        new_words = ''
        for n, j in enumerate(i):
            if n % 2 == 0:
                new_words += j.upper()
            else:
                new_words += j.lower()
                
        answer.append(new_words)
        
    return ' '.join(answer)

# 다른 사람의 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
