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
- [스택_큐](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit/%EC%8A%A4%ED%83%9D_%ED%81%90)  
- [힙](https://github.com/Hyeji-Jo/Algorithm-Study/tree/f937cc55145dfe0d4a84ea76974877c06a116dd9/%08Programmers/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EA%B3%A0%EB%93%9D%EC%A0%90%20Kit/%ED%9E%99)  
