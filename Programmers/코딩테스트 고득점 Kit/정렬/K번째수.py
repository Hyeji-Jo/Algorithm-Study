def solution(array, commands):
    answer = []
    for i in commands:
        l = 0
        l = sorted(array[i[0]-1:i[1]])[i[2]-1]
        answer.append(l)
    return answer

# 다른 사람의 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
