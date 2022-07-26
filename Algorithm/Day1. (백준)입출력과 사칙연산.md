# 알고리즘 공부 1일차

### 백준 문제 :

2527, 10718, 1000, 1001, 10998, 1008, 10869,10926, 18108, 10430, 2588

---


# 주요 문제 정리

## 1000. A+B

<br/>

> ### [문제](https://www.acmicpc.net/problem/1000)

#### 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

<br/>

> ### 예제 입력

#### 1 2

<br/>

> ### 예제 출력

#### 3

<br/>

> ### 정답 코드

```python
print(sum(map(int, input().split())))
```

<br/>

> ### 배운 개념

- ### 사용자에게 값 입력 받기

  - 예시

  ```python
  x = input()
  ```

  - x에 사용자가 입력한 값 들어감
  - x의 타입은 String

- ### split 함수

  - String의 attribute
  - 기본형 split()을 이용하면 띄어쓰기와 엔터를 기준으로 구분해준다
  - 각각의 값은 리스트로 나누어준다.
  - 예시

  ```python
  A, B = input().split()
  >> 11 12
  # A와 B 각각에 11과 12가 String 형태로 들어간다.
  ```

- ### map 함수
  - map(적용할 함수, 반복가능한 자료형) 형태로 쓰인다.
  - 예시
  ```python
  A, B = map(int, input().split())
  >> 11 12
  # A와 B에 각각 11과 12가 int 형태로 들어간다.
  ```
- ### sum 함수
  - iterable한 자료형을 받으며, numeric 해야 됨 (리스트나 튜플 처럼 인덱스 순환 접근이 가능하며 내부가 숫자로만 이루저여 있어야 함)
  - 예시
  ```python
  result = sum([1, 2, 3])
  print(result)
  >> 6
  ```

---

<br/>

## 2588. 곱셈

<br/>

> ### [문제](https://www.acmicpc.net/problem/2588)

![problem2588](./Image/2588.png)

#### (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

<br/>

> ### 예제 입력

#### 472 <br/> 385

<br/>

> ### 예제 출력

#### 2360 <br/> 3776 <br/>1416<br/>181720

<br/>

> ### 정답 코드

```python
A = input()
B = input()

print(int(A) * int(B[-1]))
print(int(A) * int(B[-2]))
print(int(A) * int(B[-3]))
print(int(A) * int(B))
```

<br/>

> ### 배운 개념

- ### 파이썬2 vs 파이썬3

  - 파이썬3에서는 int 나누기 결과가 float이다.
  - 파이썬3에서는 print문 괄호가 필수이다.
  - 파이썬3에서는 오버플로우가 없기 때문에 long 타입이 없어지고 int 타입만 남았다.

- ### // : 나눗셈 후 소수점 이하를 버리는 연산자

- ### print()문의 sep 옵션

  - sep 옵션을 통해 갈라놓을 문자를 지정할 수 있다.
  - 예시

  ```python
  print('S', 'E', 'P', sep='@')
  >> S@E@P
  print('S', 'E', 'P', sep='\n')
  >> S
     E
     P
  ```

- ### 파이썬 문자열 포매팅

  ```python
  s = 'coffee'
  n = 5
  print(f'저는 {s}를 좋아합니다. 하루에 {n}잔 마셔요.')
  >> 저는 coffee를 좋아합니다. 하루에 5잔 마셔요.
  ```

- ### 세자리 숫자 각 자리 수 구하기

  ```python
  A = '123'

  #일의 자리 수 구하기
  int(A[2]) #또는
  int(A[-1])
  ```
