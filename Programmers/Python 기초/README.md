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
  - else 사용해야 함   
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

## 4. 연산  

## 5. 반복문  

## 6. 출력  

## 7. 함수(메서드)  
- 본체 정렬
  - sort : 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬  
    ```py
    a = [1, 10, 5, 7, 6]
    a.sort()
    a #[1, 5, 6, 7, 10]
    a.sort(reverse=True) # [10, 7, 6, 5, 1]
    ```  

  - reverse : 리스트를 거꾸로 뒤집는다. desc 정렬이 아님  
    ```py
    a = [1, 10, 5, 7, 6]
    a.reverse()
    a # [6, 7, 5, 10, 1]
    ```  

- 정렬된 결과 반환
  - sorted : 순서대로 정렬, 정렬된 리스트를 반환  
    ```py
    x = [1 ,11, 2, 3]
    y = sorted(x)
    x #[1, 11, 2, 3]
    y #[1, 2, 3, 11]
    ```  
  - reversed : 거꾸로 뒤집기, iterable한 객체를 반환, 확인을 위해서는 list로 한번 더 변형 필요
    ```py
    x = [1 ,11, 2, 3]
    y = reversed(x)
    
    y # <list_reverseiterator object at 0x1060c9fd0>
    list(y) # [3, 2, 11, 1]
    ```  

