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

  # 3. 힙  
- 들어가는 자료에 우선순위를 매겨서 우선순위가 높은 자료가 먼저 나가는 자료 구조  
- **우선순위 큐**를 구현한 자료 구조로 **완전 이진트리의 일종**
  
- **_완전 이진트리_**  
  - 각 노드가 최대 2개의 자식 노드를 갖는 트리 형태  
  - 최하단 좌측 노드부터 차례로 삽입  
    
- 최소 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙  
- 최대 힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙  

- heappush(heap, item)  
  - item을 heap에 추가  
  ```py
  import heapq

  heap = []
  heapq.heappush(heap, 50)
  heapq.heappush(heap, 20)
  heapq.heappush(heap, 100)

  print(heap) # [20, 50, 100]
  ```  
  
- heappop(heap)  
  - heap에서 가장 작은 원소를 제거하고 반환  
  ```py
  removed_value = heapq.heappop(heap)

  print(removed_value) # 20
  print(heap) # [50, 100]
  ```  

- heapify(list)  
  - list를 heap으로 변환  
  ```py
  heap2 = [500, 200, 1000]
  heapq.heapify(heap2)

  print(heap2) # [200, 500, 1000]
  ```  

- 최대 힙 구현  
  - heapq는 기본적으로 **최소 힙**만 제공  
  ```py
  import heapq

  values = [1, 2, 3, 4, 5]
  heap = []
  max_heap = []

  for value in values:
      heapq.heappush(heap, -value)
  print(heap) # [-5, -4, -2, -1, -3]

  for i in range(len(heap)):
      max_heap.append(-heapq.heappop(heap))
  print(max_heap) # [5, 4, 2, 1, 3]
  ```  

# 4. 완전탐색  
- 모든 가능한 경우의 수를 탐색하여 최적의 결과를 찾는 방법을 의미  
- 보통 완전탐색 문제는 for문과 if문을 활용하거나, BFS/DFS를 활용하는 경우가 대부분  
- 입력으로 주어지는 데이터의 크기가 매우 작을때 활용  
  
## 1) 브루트 포스(Brute-Force)  
- 모든 경우를 다 탐색하면서 결과를 얻는 알고리즘   
- 경우의 수가 작을 때 사용하는 것이 일반적  
- ex) 자물쇠 암호를 찾는 경우  
  ```py
  # 배열 탐색
  def findIndex(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
  ```

## 2) 비트마스크  
- 모든 경우의 수를 이진수로 표현하여 계산해 나가는 방식  
- 하나의 변수에 여러개의 상태정보를 저장할 수 있음  
- 비트 연산을 사용하기에 빠르게 계산할 수 있어, 경우의 수가 많은 경우에 유용  

## 3) 재귀 함수  
- 자기 자신을 호출하며 모든 가능한 경우를 체크하면서 최적의 해답을 찾는 방법  

## 4) 순열  
- 서로 다른 n개 중에서 r개를 선택하여 숫자를 순서대로 뽑는 경우  

## 5) 깊이 우선 탐색(DFS)/너비 우선 탐색(BFS)  
- 그래프 자료구조에서 모든 정점을 탐색하기 위한 방법  
- 비선형 구조에서 주로 사용되며 선형 구조에서는 큰 의미를 갖지 않음  
- **DFS** : 루트 노드에서 시작하여 다음 분기로 넘어가기 전에 **해당 분기를 완벽하게 탐색**하는 방법 (스택, 재귀 활용)  
- **BFS** : 루트 노드에서 시작하여 **인접한 노드를 먼저 탐색**하는 방법 (큐 활용)  

```py
import itertools

# product, 곱집합
# product(p, q, … [repeat=1])
a = [1, 2, 3, 4]
aa = list(itertools.product(a, a))
print(aa) # [(1, 1), (1, 2), (1, 3), (1, 4), ... , (4, 1), (4, 2), (4, 3), (4, 4)]

b = list(itertools.product('1234', repeat=2))
print(b) # [('1', '1'), ('1', '2'), ('1', '3'), ... , ('4', '2'), ('4', '3'), ('4', '4')]

# permutations, 순열
# permutations(p[, r])
# 가능한 모든 순서를 반환, 반복되는 요소 없음
permutations_a = list(itertools.permutations(a))
print(permutations_a) # [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

permutations_a = list(itertools.permutations(a, 2))
print(permutations_a) # [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

permutations_a = list(itertools.permutations(a, 3))
print(permutations_a) # [(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 1, 2), (3, 1, 4), (3, 2, 1), (3, 2, 4), (3, 4, 1), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)]

# combinations, 조합
# combinatinos(p, r)
# 반복되는 요소가 없는 정렬된 순서
combinations_a = list(itertools.combinations(a, 2))
print(combinations_a) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

combinations_a = list(itertools.combinations(a, 3))
print(combinations_a) # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# combinations_with_replacement, 중복이 가능한 조합
# combinations_with_replacement(p, r)
# 조합에서 개별 요소마다 두 번 이상 반복할 수 있음
combinations_with_replacement_a = list(itertools.combinations_with_replacement(a, 2))
print(combinations_with_replacement_a) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

combinations_with_replacement_a = list(itertools.combinations_with_replacement(a, 3))
print(combinations_with_replacement_a) # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 3), (1, 2, 4), (1, 3, 3), (1, 3, 4), (1, 4, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 3), (2, 3, 4), (2, 4, 4), (3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4)]

# product, 데카르트 곱
A = [1,2,3]
list(itertools.product(A, repeat=2)) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
```

# 5. 그리드  
## 1) Kruskal 알고리즘  
- 그래프 내 모든 정점을 가장 적은 비용으로 연결하는 알고리즘  
- union-find 알고리즘을 이용  
- 프로세스  
  - 모든 간선들을 '거리(비용)'을 기준으로 오름차순 정렬  
  - 정렬된 순서에 맞게 그래프에 포함  
  - 포함시키기 전, 사이클을 형성하는 경우 간선을 포함하지 않음  
