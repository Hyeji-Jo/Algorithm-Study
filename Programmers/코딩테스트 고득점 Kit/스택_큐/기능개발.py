# 시간 초과 풀이
def solution(progresses, speeds):
    answer = []
    day = []
    
    for p,s in zip(progresses,speeds):
        day.append((100-p)/s)
        
    for n,i in enumerate(day):
        tmp = 0
        if int(day[n]) > int(day[n-1]) or n==0:
            tmp += 1
        else:
            day.append(tmp)
    return answer

# 정답 코드
from collections import deque

def solution(progress, speeds):
    answer = []
    days = deque()

    for i in range(len(progress)):
        x = (100 - progress[i]) / speeds[i]

        if x == int(x):
            days.append(int(x))
        else:
            days.append(int(x)+1)

    while days:
        temp = days.popleft()
        count = 1
        
        while days and temp >= days[0]:
            days.popleft()
            count += 1
        answer.append(count)

    return answer

# 다른 사람의 풀이
def solution(progresses, speeds):
    answer = []
    days = 0 # 날짜 세기
    cnt = 0 # 완료된 기능
    while len(progresses) > 0:
    	# 기능의 진행상황과 그 동안 지난 날짜만큼의 speed를 구해서 더하기
        if(progresses[0]+days*speeds[0])>=100:
            # 완료되면 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)
            # 완료된 기능 수
            cnt += 1
        else:
        	# 만약 완료된 기능이 있다면 answer에 더해주고 0으로 초기화
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            # 완료된 기능이 없으면 days 추가
            else:
                days+=1
    answer.append(cnt)
    return answer
