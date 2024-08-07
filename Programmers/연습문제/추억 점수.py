# 도움 받은 풀이
def solution(name, yearning, photo):
    answer = []
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    for phic in photo:
        score = 0
        for person in phic:
            if person in yearning_dict:
                score += yearning_dict[person]
        answer.append(score)
    
    return answer

# 다른 사람의 풀이
def solution(name, yearning, photo):
    dictionary = dict(zip(name,yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores
