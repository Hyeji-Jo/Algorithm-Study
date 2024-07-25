def solution(s):
    answer = True
    if len(s) ==4 or len(s)==6:
        try:
            int(s)
            answer = True
        except:
            answer = False
    else:
        answer = False
    return answer

# 다른 사람의 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]

def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 
