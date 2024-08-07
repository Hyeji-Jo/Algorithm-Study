# 다른 사람의 풀이
from collections import deque

def is_valid(s):
    stack = []
    matching = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in '}])':
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def solution(s):
    s_que = deque(s)
    valid_count = 0
    
    for _ in range(len(s)):
        if is_valid(''.join(s_que)):
            valid_count += 1
        s_que.rotate(-1)

    return valid_count
