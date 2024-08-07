# 도움 받은 코드
from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 원하는 제품과 수량을 Counter로 저장합니다.
    want_counter = Counter()
    for w, n in zip(want, number):
        want_counter[w] = n
    
    # 슬라이딩 윈도우로 10일 간격으로 비교합니다.
    for i in range(len(discount) - 9):
        # 현재 10일 간격의 제품들을 카운트합니다.
        current_window = discount[i:i+10]
        current_counter = Counter(current_window)
        
        # 현재 카운터와 원하는 카운터를 비교합니다.
        if current_counter == want_counter:
            answer += 1
    
    return answer


# 다른 사람의 풀이
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer
