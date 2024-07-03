# 시간 초과 풀이
def solution(phone_book):
    answer = True
    phone_book.sort()
    for n,i in enumerate(phone_book):
        for j in phone_book[n+1:]:
            if j.startswith(i):
                return False
    return answer

# 통과한 풀이
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return answer

# 해시 활용 풀이
def solution(phone_book): 

    # 1.Hash map생성
    hash_map = {} 
    for nums in phone_book: 
        hash_map[nums] = 1 
    
    # 2.접두어가 Hash map에 존재하는지 찾기 
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != nums:       
                return False 
                
    return True
