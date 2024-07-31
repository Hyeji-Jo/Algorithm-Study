def solution(food):
    answer = ''
    
    for n, i in enumerate(food[1:]):
        answer+= str(n+1)*(i//2)
    
    reverse_answer = ''.join(list(reversed(answer)))
        
    return answer+'0'+reverse_answer


# 다른 사람의 풀이
def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]



def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
