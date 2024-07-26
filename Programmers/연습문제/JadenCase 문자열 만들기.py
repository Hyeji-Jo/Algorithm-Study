# 시간 초과
def solution(s):
    answer = []
    lst = s.split(' ')
    for i in lst:
        change = i.lower()
        if change[0].isdigit():
            pass
        else:
            change = change.replace(change[0], change[0].upper(),1)
            
        answer.append(change)
    return ' '.join(answer)

# 수정된 코드
def solution(s):
    answer = []
    lst = s.split(' ')
    for i in lst:
        # 첫 문자가 알파벳인 경우 대문자로 변환, 나머지는 소문자로 변환
        if i and not i[0].isdigit():
            change = i[0].upper() + i[1:].lower()
        else:
            change = i.lower()
            
        answer.append(change)
    return ' '.join(answer)

# 다른 풀이
def solution(s):
    # 문자열을 공백 단위로 split 하되, 공백을 유지하기 위해 split(' ') 사용
    words = s.split(' ')
    # 각 단어를 JadenCase로 변환
    jaden_case_words = [word.capitalize() for word in words]
    # 변환된 단어들을 다시 공백 단위로 join 하여 결과 문자열 생성
    result = ' '.join(jaden_case_words)
    return result
