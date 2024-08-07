def solution(elements):
    answer = 0
    ex_elements = elements+elements
    elements_lst = []
    
    for i in range(0, len(elements)):
        for j in range(1, len(elements)+1):
            value = sum(ex_elements[i:i+j])
            elements_lst.append(value)
    return len(set(elements_lst))


# 간결한 풀이
def solution(elements):
    n = len(elements)
    # 원형 수열을 나타내기 위해 elements를 두 번 반복하여 확장합니다
    extended_elements = elements + elements
    unique_sums = set()
    
    # 슬라이딩 윈도우로 연속 부분 수열의 합을 구합니다
    for length in range(1, n + 1):
        for start in range(n):
            segment_sum = sum(extended_elements[start:start + length])
            unique_sums.add(segment_sum)
    
    return len(unique_sums)
