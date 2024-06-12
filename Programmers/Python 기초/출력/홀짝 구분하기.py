a = int(input())

if a %2 ==0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 다른 사람의 풀이
n = int(input())
print(f"{n} is odd" if n % 2 else f"{n} is even")
