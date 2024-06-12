## 본체 정렬
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

## 정렬된 결과 반환
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
