# 도움 받은 풀이
def solution(n, words):
    answer = [0, 0]
    use_words = []
    start_word = words[0]
    use_words.append(start_word)

    for i in range(1, len(words)):
        word = words[i]
        
        if word not in use_words and word.startswith(start_word[-1]):
            use_words.append(word)
            start_word = word  # Update start_word to the current word
        else:
            route = (i // n) + 1
            who = (i % n) + 1
            answer = [who, route]
            break  # Stop the loop if a player is found to be out

    return answer

# 더 간결한 코드
def solution(n, words):
    used_words = {words[0]}
    
    for i in range(1, len(words)):
        if words[i] in used_words or words[i][0] != words[i-1][-1]:
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(words[i])
    
    return [0, 0]

# 다른 사람의 풀이
def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer
