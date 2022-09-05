# 알고리즘 공부 13일차

https://covenant.tistory.com/224

- Par1. 튼튼한 기본기

# 백준 주요 문제 정리 :

3460, 2309

---

## 3460. 이진수

<br/>

> ### [문제](https://www.acmicpc.net/problem/3460)

#### <br/>양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

<br/>

> ### Python3 코드

```python
t = int(input())
# t개의 테스트 케이스 주어짐
for _ in range(t):
    binary_number = bin(int(input()))[2:]
    for idx, value in enumerate(binary_number[::-1]):
        if value == "1":
            print(idx, end=" ")
```

<br/>

> ### Python3 코드 풀이

### 1. 문제 요약

이 문제는 n의 이진수를 구해 1의 위치를 출력하는 프로그램이다. 자릿수는 가장 낮은 자릿수가 0이 된다.
<br/>

처음에는 for문을 돌면서 2로 나누면서 리스트에 각 자릿수를 저장해주었다. 그러나 이렇게 풀 경우 가장 큰 입력값이 입력되면 리스트의 범위를 넘어가기 때문에 메모리 초과 오류가 난다. <br/>그래서 다른 분의 답을 참고해서 파이썬에서 제공하는 이진수 함수인 bin 함수를 이용해서 문제를 풀어줬다.

### 2. 이진수 값 구해주기

```python
for _ in range(t):
    binary_number = bin(int(input()))[2:]
```

사용자로부터 입력받은 값을 정수형으로 변환 후 bin함수를 이용해서 이진수로 바꿔준다. bin 함수를 사용하면 '0b1010'과 같은 값이 나오기 때문에 `[2:]`를 이용해서 슬라이싱해줘야 한다.

### 3. 1의 위치 구하기

```python
 for idx, value in enumerate(binary_number[::-1]):
        if value == "1":
            print(idx, end=" ")
```

원소가 1인 경우의 인덱스를 출력해줘야 하기 때문에 enumerate 함수를 이용해서 반복문을 적어줬다.

이 문제는 이진수의 낮은 자릿수부터 출력해야하기 때문에 `[::-1]`로 리스트를 뒤집어주었다.<br/>bin 함수는 문자열을 반환하기 때문에 조건문에서 숫자 1이 아닌 문자 "1"을 사용해야 한다.

### 4. enumerate 함수

반복문 사용시 몇 번째 반복문인지 확인이 필요한 경우가 있는데, 이때 enumerate 함수를 사용한다. 이 함수는 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환한다. -> `(인덱스, 값)` <br/>아래와 같이 사용하면 된다.

```python
for idx, value in enumerate(리스트)
```

### 5. 리스트 순서 뒤집기

1. List 역순으로 읽어오는 루프 사용할때

리스트의 값을 역으로 루프를 돌리는 경우 다음과 같이 작성할 수 있다.

```python
for item in my_list[::-1]
```

2. List 역순으로 바꾸기

- reverse() 함수는 아무런 값도 반환하지 않지만 리스트 자체를 역순으로 변경해준다.

```python
my_list.reverse()
```

- reversed() 함수는 리스트의 역순을 반환해준다. 리스트의 원본을 변경하지 않는다.

```python
reversed(my_list)
```

---

## 2309. 일곱 난쟁이

<br/>

> ### [문제](https://www.acmicpc.net/problem/2309)

#### <br/>왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.<br/>아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.<br/>아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

<br/>

> ### Python3 코드

```python
height_list = []
one = 0
two = 0
is_break = False

for _ in range(9):
    height_list.append(int(input()))

for i in range(0, 8):
    for j in range(i+1, 9):
        if height_list[i] + height_list[j] == sum(height_list) - 100:
            one = height_list[i]
            two = height_list[j]
            is_break = True
            break
    if is_break:
        break
height_list.remove(one)
height_list.remove(two)
height_list.sort()
for i in height_list:
    print(i)
```

<br/>

> ### Python3 코드 풀이

### 1. 문제 요약

이 문제는 일곱 난쟁이의 키의 합이 100이라는 사실을 이용하여 일곱 난쟁이가 아닌 두명은 뺀 후 일곱 난쟁이를 키에 대해 오름차순으로 출력하는 문제이다.
<br/>

일곱난쟁이의 키의 합이 100이기 때문에 입력받은 아홉 난쟁이들의 키의 합에서 100을 뺀 수가 일곱난쟁이가 아닌 두 난쟁이의 키의 합이 된다. <br/>따라서 for문을 돌면서 모든 조합의 난쟁이 두쌍의 키의 합을 계산해봐야 한다.

### 2. 변수 설명

```python
height_list = []
one = 0
two = 0
is_break = False
```

height_list는 난쟁이들의 키를 저장하는 변수이다.
one과 two는 일곱 난쟁이가 아닌 난쟁이 두명의 각각의 키를 저장하는 변수이다.
is_break는 이중 for문을 벗어나기 위한 장치로, 내부 for문에서 벗어난다면 외부 for문에서도 벗어날 수 있게해준다.

### 3. 난쟁이 입력받기

```python
for _ in range(9):
    height_list.append(int(input()))
```

for문을 이용해서 난쟁이 9명의 키를 입력받아 리스트에 추가해준다.

### 4. 일곱 난쟁이가 아닌 난쟁이 두명 구하기

```python
for i in range(0, 8):
    for j in range(i+1, 9):
        if height_list[i] + height_list[j] == sum(height_list) - 100:
            one = height_list[i]
            two = height_list[j]
            is_break = True
            break
    if is_break:
        break
```

for문의 i와 j는 인덱스를 나타내는 변수이다.
외부 for문은 원소와 그 다음 원소를 조합해줘야 하기 때문에 마지막 인덱스보다 하나 앞까지만 돈다.
내부 for문은 i와 그 다음 인덱스들을 조합시켜줘야 하기 때문에 i+1부터 마지막 인덱스까지 돈다.
만약 i번째와 j번째 난쟁이의 키의 합이 9명의 키의 합에서 100을 뺀 수와 같다면 그 둘이 일곱난쟁이가 아닌것으로 판명난다. 그래서 one과 two 변수에 그 두명의 키를 저장해주고 내부 for문이 종료된다. is_break 변수가 True가 됐으므로 외부 for문도 종료된다.

### 5. 답 구하기

```python
height_list.remove(one)
height_list.remove(two)
height_list.sort()
for i in height_list:
    print(i)
```

문제의 정답은 일곱 난쟁이들을 키에 대해 오름차순으로 출력해야 한다.
그래서 앞에서 구한 두 난쟁이를 난쟁이 리스트에서 제거해준다.
sort함수를 이용해서 난쟁이들을 오름차순으로 정렬해준 후 for문을 통해 답을 출력해준다.

### 6. 리스트 요소 제거하기

#### 1. 인덱스로 제거하기

- del 리스트명[인덱스]
  - del을 통한 삭제는 슬라이싱을 통해 여러개를 한번에 삭제할수도 있다.
  ```python
  user_list = ['Jason' , 'Smith', 'Kevin']
  del user_list[1:3]
  print(user_list)
  >> ['Jason']
  ```
- 리스트명.pop(인덱스)
  - 만약 매개변수가 없다면 자동으로 -1값이 들어가서 리스트의 맨 마지막 요소가 제거된다.

#### 2. 값으로 제거하기

- 리스트.remove(값)
  - 리스트에서 같은 값을 가지는 원소를 지워준다. 하지만 모든 값을 지워주지는 않고 가장 먼저 발견된 요소를 지워준다.
  - 만약 같은 값을 가지는 모든 요소를 제거하고 싶다면 반복문을 통해 삭제해줘야 한다.
