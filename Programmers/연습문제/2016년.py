# 도움 받은 코드
def solution(a, b):
    answer = ''
    # 각 월의 일수를 정의합니다. (윤년 고려)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 요일 목록을 정의합니다.
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    
    # 1월 1일부터 해당 날짜까지의 총 일수를 계산합니다.
    total_days = sum(days_in_month[:a-1]) + b - 1
    
    # 요일을 계산합니다.
    answer = day[total_days % 7]
    
    return answer
