import re
from collections import Counter

def get_multiset(s):
    s = s.lower()  # 문자열을 소문자로 변환
    multi_set = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]  # 두 글자씩 추출
        if re.match(r'^[a-z]{2}$', pair):  # 유효한 두 글자 쌍인지 확인
            multi_set.append(pair)  # 다중집합에 추가
    return multi_set

def solution(str1, str2):
    set1 = get_multi(str1)
    set2 = get_multi(str2)
    
    # Use Counter to count occurrences
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    # Calculate intersection and union
    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())
    
    # Calculate Jaccard similarity
    if union == 0:
        return 65536  # Both sets are empty
    jaccard_similarity = intersection / union
    
    # Return result scaled by 65536 and truncated to integer
    return int(jaccard_similarity * 65536)
