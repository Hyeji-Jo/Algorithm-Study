def solution(k, dungeons):
    import itertools
    answer = 0
    
    for permute in itertools.permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        
        for i in permute:
            if hp >= i[0]:
                cnt+=1
                hp -= i[1]
            else:
                break
                
        if cnt > answer:
            answer = cnt
        
    return answer
