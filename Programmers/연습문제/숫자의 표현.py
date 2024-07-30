# 다른 사람의 풀이 - 완전 탐색
def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer+= 1
                break
            elif sum > n:
                break
    return answer

# 패턴을 활용한 풀이
  def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
