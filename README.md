# Algorithm-Study
코딩 테스트 공부


## [프로그래머스](https://programmers.co.kr/)  
### Python 기초 [[개념⚒️]](https://github.com/Hyeji-Jo/Algorithm-Study/blob/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/README.md) 
  
- [리스트(배열)](https://github.com/Hyeji-Jo/Algorithm-Study/tree/fa9f3c4e586bebff91c983b6d14fc97374f476cd/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EB%A6%AC%EC%8A%A4%ED%8A%B8(%EB%B0%B0%EC%97%B4))  
  ```py
  # 리스트 원소 제거 : .remove(x)
  arr.remove(i)
  ```  
  
- [문자열](https://github.com/Hyeji-Jo/Algorithm-Study/tree/8a2d055237545b9842580e41a899d4410143f2bd/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EB%AC%B8%EC%9E%90%EC%97%B4)  
  ```py
  # 접두사 : .startswith(x)
  result = str.startswith('final')
  print(result) #True

  # 접미사 : .endswith(x)
  result = str.endswith('exam')

  # 공백으로 구분하기 : .split()
  my_string = "i love you"
  result = my_string.split()     # result = ["i", "love", "you"]

  # 영어를 숫자로 바꾸기 : ord(x)
  ord('a')  # 97
  ```  
  
- [조건문](https://github.com/Hyeji-Jo/Algorithm-Study/tree/8a2d055237545b9842580e41a899d4410143f2bd/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EC%A1%B0%EA%B1%B4%EB%AC%B8)  
  ```py
  # 한줄 if문 (else 사용해야함)
  vhicle = "버스" if money > 1000 else "걷기"

  # 한줄 for문
  c = [i ** 2 for i in range(10)]

  # if+for문
  print([i**2 for i in range(21) if (i**2) % 2 == 0])
  ```  
  
- [연산](https://github.com/Hyeji-Jo/Algorithm-Study/tree/25646a028a4db915fbe5a99878f60782ccc9c7c9/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EC%97%B0%EC%82%B0)  
  ```py
  # 몫
  3//2  #1

  # 나머지
  2%3  #2

  # 원소의 곱 : prod(x)
  from math import prod
  prod(num_list)
  ```  
  
- [반복문](https://github.com/Hyeji-Jo/Algorithm-Study/tree/c226ad25f6b025d1a11a10195c3ccadb28a67d4f/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EB%B0%98%EB%B3%B5%EB%AC%B8)  
  
- [출력](https://github.com/Hyeji-Jo/Algorithm-Study/tree/c226ad25f6b025d1a11a10195c3ccadb28a67d4f/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%EC%B6%9C%EB%A0%A5)  
    
- [함수(메서드)](https://github.com/Hyeji-Jo/Algorithm-Study/tree/c226ad25f6b025d1a11a10195c3ccadb28a67d4f/%08Programmers/Python%20%EA%B8%B0%EC%B4%88/%ED%95%A8%EC%88%98(%EB%A9%94%EC%84%9C%EB%93%9C))  
  ```py
  # 본체 정렬 : .sort(x)
  a = [1, 10, 5, 7, 6]
  a.sort()
  a #[1, 5, 6, 7, 10]
  a.sort(reverse=True) # [10, 7, 6, 5, 1]

  # 리스트 뒤집기 : .reverse(x)
  a = [1, 10, 5, 7, 6]
  a.reverse()
  a # [6, 7, 5, 10, 1]

  # 정렬된 결과 반환 : sorted(x)
  x = [1 ,11, 2, 3]
  y = sorted(x)
  x #[1, 11, 2, 3]
  y #[1, 2, 3, 11]

  # 뒤집은 결과 반환 : reversed(x) -> list(x)
  x = [1 ,11, 2, 3]
  y = reversed(x)
  y # <list_reverseiterator object at 0x1060c9fd0>
  list(y) # [3, 2, 11, 1]
  ```  
  

### 코딩테스트 고득점 KIT [[개념⚒️]](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit) 
- [해시](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit/%ED%95%B4%EC%8B%9C)  
  - 데이터의 효율적 관리를 목적으로 임의의 길이인 데이터를 고정된 길이의 데이터로 매핑하는 것  
    - 장점 : 자료의 검색, 읽기, 저장 속도가 빠르며, 보안에도 많이 사용됨  
    - 단점 : 순서가 있는 배열에 어울리지 않으며, 충동을 해결할 방법 필요   
  ```py
  students = {'kim': 17, 'lee': 15, 'park': 18}
  
  # 키값 추출 : .keys()
  students.keys()  # >> dict_keys(['kim', 'lee', 'park'])

  # 값 추출 : .values()

  # 키로 값 얻기 : .get(x)
  print(students.get('kim')) # 17

  # 키+값 : .items()
  print(students.items()) # dict_items([('kim', 17), ('lee', 15), ('park', 18)])

  # 한쌍 지우기 : del x
  del students['kim']
  print(students) # {'lee': 15, 'park': 18}

  # 모두 지우기 : .clear()
  students.clear()
  print(students) # ""
  ```  
  
- [스택_큐](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit/%EC%8A%A4%ED%83%9D_%ED%81%90)
  - 스택 : 후입선출의 원칙, 마지막에 입력된 데이터가 가장 먼저 제거 (리스트 활용)  
  - 큐 : 선입선출의 원칙 (덱 활용)  
  ```py
  from collections import deque
  
  dq = deque() # 덱 생성
  
  dq.append(1) # dq에 뒤로 데이터 넣기
  dq.appendleft(2) # dq에 앞으로 데이터 넣기
  
  print(dq) # deque([2, 1])
  
  print(dq.pop()) # 1, 맨 뒤의 데이터 꺼내기
  print(dq.popleft()) # 2, 맨 앞의 데이터 꺼내기
  ```  
  
- [힙](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit/%ED%9E%99)  
- 자료에 우선순위를 매겨서 우선순위가 높은 자료가 먼저 나가는 구조 (=우선순위 큐)  
  ```py
  import heapq
  heap = []
  
  # item을 heap에 추가 : heapq.heappush(x, num)
  heapq.heappush(heap, 50)
  heapq.heappush(heap, 20)
  heapq.heappush(heap, 100)
  print(heap) # [20, 50, 100]

  # 가장 작은 원소 제거 : heapq.heappop(x)
  removed_value = heapq.heappop(heap)
  print(removed_value) # 20
  print(heap) # [50, 100]

  # list를 heap으로 변환 : heapq.heapify(x)
  ```  
   
