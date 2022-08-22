# 알고리즘 공부 13일차

https://covenant.tistory.com/224

- Par1. 준비운동

### 백준 문제 :

3460

---

# 주요 문제 정리

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
