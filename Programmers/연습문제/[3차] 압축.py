# 다른 사람의 코드
def solution(msg):
    answer = []
    alpha = {chr(i+65):i+1 for i in range(26)}
    
    while True:
        if msg in alpha:
            answer.append(alpha[msg])
            break
        
        else:
            for j in range(1, len(msg)+1):
                if msg[0:j] not in alpha:
                    answer.append(alpha[msg[0:j-1]])   
                    alpha[msg[0:j]] = len(alpha)+1
                    msg = msg[j-1:]
                    break
        
    return answer
