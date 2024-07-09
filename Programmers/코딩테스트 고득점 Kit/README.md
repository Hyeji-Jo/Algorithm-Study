# 1. 해시
## 1) 중복제거
- set()

## 2) 해시 원리  

- 해시함수란 데이터의 효율적 관리를 목적으로 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 것  
  - 매핑 전 원래 데이터의 값 : 키(key)  
  - 매핑 후의 데이터의 값 : 해시값(hash value)  
  - 매핑하는 과정자체 : 해싱(hashing)
    
  예를 들어 아래처럼 키와 값이 있을 때, 
  
  |**키(key)**|**값(value)**|
  |------|---------|
  |"a"|"apple"|
  |"b"|"banana"|
  |"c"|"cherry"|  
  
  변환되는 테이블은 아래와 같다  
  
  |**키(key)**|변환 과정|**인덱스(index)**|**값(value)**|
  |-----------|-------|---------|---------|
  |“a”| → 해시 함수(97 % 3) → |0|cherry|
  |“b”| → 해시 함수(98 % 3) → |1|apple|
  |“c”| → 해시 함수(99 % 3) → |2|banana|  


## 3) 해시 특징  
- 장점  
  - 적은 리소스로 많은 데이터를 효율적으로 관리할 수 있음  
  - 자료의 검색, 읽기, 저장 속도가 빠름  
  - 자료가 중복되는지 확인하기 쉬움  
  - 키(key)와 해시값(hash value)이 연관성이 없어 보안에도 많이 사용됨  
 
- 단점  
  - 저장 공간이 더 필요함  
  - 충돌을 해결할 방법 필요  
  - 순서가 있는 배열에는 어울리지 않음
 
## 4) Dictionary(파이썬에서 hash table 활용의 예)
- keys  
  - 키값 추출  
  ```py
  students = {'kim': 17, 'lee': 15, 'park': 18}

  # key 출력
  print(students.keys()) # >> dict_keys(['kim', 'lee', 'park'])  

  # key 순서대로 출력
  for student in students.keys():
    print(student)
  # kim
  # lee
  # park
  ```  
  
- values  
  - 딕셔너리의 값 추출
  ```py
  # value 출력
  print(students.values())

  # value 순서대로 출력
  for age in students.values():
  	print(age)
  ```

- get  
  - 딕셔너리 키로 값 얻기
  ```py
  print(students.get('kim')) # 17
  ```  
  
- items  
  - 딕셔너리 키, 값 합쳐서 뽑기
  ```py
  print(students.items()) # dict_items([('kim', 17), ('lee', 15), ('park', 18)])

  for student_info in students.items():
	  print(student_info)
  ```

- del  
  - 딕셔너리에서 키, 값 한쌍 지우기
  ```py
  del students['kim']
  print(students) # {'lee': 15, 'park': 18}
  ```

- clear  
  - 모두 지우기
  ```py
  students.clear()
  print(students) # ""
  ```  

# 2.스택/큐  
- 스택(Stack)  
  - 후입선출(Last in first out) 원칙
  - 가장 마지막에 입력된 데이터가 가장 먼저 제거되는 구조
  - 파이썬의 리스트가 사실상 스택의 모든 연산을 지원  
- 큐(Queue)  
  - 선입선출(Firt in first out) 원칙  
  - 파이썬에서 큐를 구현할때는 덱을 이용
  ```py
  from collections import deque

  dq = deque() # 덱 생성

  dq.append(1) # dq에 뒤로 데이터 넣기
  dq.appendleft(2) # dq에 앞으로 데이터 넣기

  print(dq) # deque([2, 1])

  print(dq.pop()) # 1, 맨 뒤의 데이터 꺼내기
  print(dq.popleft()) # 2, 맨 앞의 데이터 꺼내기
  ```
