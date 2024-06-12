## 한줄 if문  
  ```py
  money = int(input())
  vhicle = "버스" if money > 1000 else "걷기"
  print(f"{vhicle}를 이용하여 집에 가시오.")
  ```  

## 한줄 for문  
  ```py
  c = [i ** 2 for i in range(10)]
  ```  

## if + for문  
  ```py
  print([i**2 for i in range(21) if (i**2) % 2 == 0])
  ```  
