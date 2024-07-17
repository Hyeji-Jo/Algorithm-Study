# 다른 사람의 풀이
def solution(triangle):
    answer = 0
    # 층 인덱스 만들기
    floor = len(triangle)-1
    
    while floor > 0:
        for i in range(floor):
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1
        
    answer = triangle[0][0]
    return answer


def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])
