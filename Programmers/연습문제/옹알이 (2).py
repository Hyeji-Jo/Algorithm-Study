# 다른 사람의 풀이
import re

def solution(babbling):
    answer = 0
    # 발음할 수 있는 단어 패턴
    pattern = re.compile(r'^(aya|ye|woo|ma)+$')
    
    # 연속된 발음이 없는지 확인하기 위한 패턴
    invalid_pattern = re.compile(r'(aya|ye|woo|ma)\1')
    
    for word in babbling:
        # 발음할 수 있는 단어인지 확인하고, 연속된 발음이 없는지 확인
        if pattern.match(word) and not invalid_pattern.search(word):
            answer += 1
            
    return answer


def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
