# 다른 사람의 풀이
import re
from collections import Counter

def solution(s):
    numbers = re.findall(r'\d+', s)
    counter = Counter(numbers)
    sorted_number = [int(num) for num,_ in counter.most_common()]
    return sorted_number

# 다른 사람의 풀이
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
