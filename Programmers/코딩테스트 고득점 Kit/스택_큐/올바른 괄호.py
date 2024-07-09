def solution(s):
    box = []
    
    for i in s:
        if i == '(':
            box.append(i)
        else:
            if box == [] :
                return False
            else:
                box.pop()
        
    

    return box == []


# 다른 사람의 풀이
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0


def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0
