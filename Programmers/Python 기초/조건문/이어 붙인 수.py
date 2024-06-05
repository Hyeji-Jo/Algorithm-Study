def solution(num_list):
    answer = 0
    a=[]
    b=[]
    for i in num_list:
        if i % 2 == 0:
            a.append(str(i))
        else:
            b.append(str(i))
    
    asum = ''.join(a)
    bsum = ''.join(b)
    
    answer = int(asum)+int(bsum)
    return answer

# 다른 사람 코드
def solution(num_list):
    answer = 0
    a=""#홀수
    b=""#짝수
    for i in num_list:
        if i%2!=0:
            a+=str(i)
        else:
            b+=str(i)
    return int(a)+int(b)
