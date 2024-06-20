def solution(myString, pat):
    myString = myString.replace('A', 'b').replace('B', 'a')
            
    return int(pat.lower() in myString)

# 다른 사람의 풀이
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))
