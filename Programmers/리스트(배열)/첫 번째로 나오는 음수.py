def solution(num_list):
    answer = 0
    

    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
        
        if answer == 0:
            answer =- 1 

    
    return answer


# 다른 사람 코드

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i]<0:return i
    return -1
