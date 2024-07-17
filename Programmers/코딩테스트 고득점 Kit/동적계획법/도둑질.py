# 다른 사람의 풀이
def solution(money):
    dp1 = [0]*len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0],money[1])
    
    # 첫 번째 집을 무조건 터는 경우
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])
        
    dp2 = [0]*len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    
    # 마지막 집을 무조건 터는 경우
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])
    return max(max(dp1), max(dp2))



def solution(money):
    answer = 0

    dp1 = [] # 첫 집을 털었을 때
    dp2 = [] # 첫 집을 안 털고 두 번째 집을 털었을 때
    dp3 = [] # 첫 집과 두 번째 집을 안 털었을 때
    for i in money:
        dp1.append(0)
        dp2.append(0)
        dp3.append(0)
    dp1[0] = money[0]
    dp1[1] = dp1[0]
    dp2[1] = money[1]

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
        dp3[i] = max(dp3[i - 1], dp3[i - 2] + money[i])
    e = len(money) - 1
    dp1[e] = dp1[e - 1]
    dp2[e] = max(dp2[e - 1], dp2[e - 2] + money[e])
    dp3[e] = max(dp3[e - 1], dp3[e - 2] + money[e])
    answer = max(dp1[e], dp2[e], dp3[e])

    return answer
