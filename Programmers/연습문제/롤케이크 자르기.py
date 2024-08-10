# 다른 사람의 풀이
def solution(topping):
    answer = 0
    
    from collections import defaultdict
    
    # 전체 토핑의 개수
    total = len(topping)
    
    # 왼쪽 조각의 토핑 종류
    left_cnt = defaultdict(int)
    # 오른쪽 조각의 토핑 종류
    right_cnt = defaultdict(int)
    
    # 초기 오른쪽 조각의 토핑 종류를 전체에서 계산
    for t in topping:
        right_cnt[t] += 1
        
    # 왼쪽 조각과 오른쪽 조각의 토핑 종류 개수
    left_unique_count = 0
    right_unique_count = len(right_cnt)
    
    # 슬라이딩 윈도우로 각 위치에서 공평한지 확인
    for i in range(total - 1):
        current = topping[i]
        
        # 왼쪽 조각의 토핑 업데이트
        if left_cnt[current] == 0:
            left_unique_count += 1
        left_cnt[current] += 1
        
        # 오른쪽 조각의 토핑 업데이트
        right_cnt[current] -= 1
        if right_cnt[current] == 0:
            right_unique_count -= 1
        
        # 공평한 경우 카운트 증가
        if left_unique_count == right_unique_count:
            answer += 1
    
    return answer


# 다른 사람의 풀이2
from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer
