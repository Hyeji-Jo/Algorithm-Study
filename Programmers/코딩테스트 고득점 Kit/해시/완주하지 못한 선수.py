# 시간 초과 풀이
def solution(participant, completion):

    for i in completion:
        participant.remove(i)
    answer = participant[0]

    return answer

# 통과한 풀이
def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
        
    return participant[-1]


# 다른 사람의 풀이
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    
    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hashDict[sumHash]
