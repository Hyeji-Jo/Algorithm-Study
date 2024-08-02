# 도움 받은 코드
def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a_bin = bin(a)[2:].zfill(n)
        b_bin = bin(b)[2:].zfill(n)
        
        result = ''
        
        for a_c, b_c in zip(a_bin, b_bin):
            if a_c=='1' or b_c=='1':
                result += '#'
            else:
                result += ' '
        answer.append(result)

    return answer
