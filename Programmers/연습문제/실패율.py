# 도움 받은 풀이
def solution(N, stages):
    answer = []
    stages_fail = {}
    total_players = len(stages)
    
    for i in range(1, N+1):
        if i in stages:
            count = stages.count(i)
            stages_fail[i] = count/total_players
            total_players -= count
        else:
            stages_fail[i] = 0
    
    sorted_stages = sorted(stages_fail.items(), key=lambda x: (-x[1], x[0]))
    answer = [stage for stage, _ in sorted_stages]
    
    return answer


# 다른 사람의 풀이
def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer
