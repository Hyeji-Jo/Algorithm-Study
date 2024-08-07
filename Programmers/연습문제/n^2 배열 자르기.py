# 다른 사람의 풀이
def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        # 행 인덱스와 열 인덱스를 계산합니다
        row = i // n
        col = i % n
        # 행과 열 인덱스 중 더 큰 값을 사용하여 값을 결정합니다
        answer.append(max(row, col) + 1)

    return answer
