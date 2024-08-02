def solution(k, score):
    answer = []
    board = []
    
    for s in score:
        board.append(s)
        board.sort(reverse=True)  # 내림차순으로 정렬하여 상위 점수들이 앞에 오도록
        if len(board) > k:
            board.pop()  # k개 초과하면 최하위 점수 제거
        answer.append(board[-1])  # 명예의 전당 최하위 점수 기록
    
    return answer

# 다른 사람의 풀이
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
