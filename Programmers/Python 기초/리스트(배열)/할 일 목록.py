def solution(todo_list, finished):
    answer = []
    for n, i in enumerate(todo_list):
        if not finished[n]:
            answer.append(i)
    return answer

# 다른 사람의 풀이
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]
