def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr

# 다른 사람의 풀이
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]
