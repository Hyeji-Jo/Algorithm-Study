# Python 기초 개념  

## 1. 리스트(배열)  
- 몫  
  ```py
  3//2
  # 1 
  ```

- 나머지
  ```py
  2%3
  # 2 
  ```

## 2. 문자열  
- 접두사 : startswith  
  - 특정 문자로 시작하는지 확인하는 함수  
  - 리턴 값은 true 혹은 false  
  ```py
  str = 'final exam'
  
  result = str.startswith('final')
  print(result) #True
  ```

- 접미사 : endswith  
  ```py
  str = 'final exam'
  
  result = str.endswith('exam')
  print(result) #True
  ```

## 3. 조건문  
- 한줄 if문  
  ```py
  money = int(input())
  vhicle = "버스" if money > 1000 else "걷기"
  print(f"{vhicle}를 이용하여 집에 가시오.")
  ```  

- 한줄 for문  
  ```py
  c = [i ** 2 for i in range(10)]
  ```  

- if + for문  
  ```py
  print([i**2 for i in range(21) if (i**2) % 2 == 0])
  ```  
