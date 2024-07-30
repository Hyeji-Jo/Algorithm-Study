# 다른 사람의 풀이
def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return int(answer, 3)
  
