a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)

# 다른 사람의 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
