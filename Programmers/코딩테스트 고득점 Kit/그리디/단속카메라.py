# 다른 사람의 풀이
def solution(routes):
    answer = 0
    # 진출 시점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    # -30001부터 위치 찾기
    camera = -30001
    
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
