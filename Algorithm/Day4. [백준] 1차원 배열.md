# 알고리즘 공부 4일차

### 백준 문제 :

10818, 2562

---

# 주요 문제 정리

## 2562. 최댓값

<br/>

> ### [문제](https://www.acmicpc.net/problem/2562)

#### 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오. <br/>예를 들어, 서로 다른 9개의 자연수 <br/>3, 29, 38, 12, 57, 74, 40, 85, 61<br/>이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

<br/>

> ### 예제 입출력

![problem](./Image/2562.PNG)

<br/>

> ### 내 코드 [ 메모리 : 30840 KB / 시간 72ms ]

```python
import sys
list = []
for _ in range(9):
    list.append(int(sys.stdin.readline()))
max = max(list)
print(max)
for i in range(9):
    if(list[i] == max):
        print(i+1)
        break
```

<br/>

> ### POINT!

## 1. 9개의 입력을 어떻게 리스트에 넣을 것인가

두 가지 방법이 있다.
<br/>1. for문을 돌면서 list에 append를 해준다. (내가 짠 코드 처럼)
<br/>2. 리스트 안에 for문을 포함한다.

`list = [int(sys.stdin.readline()) for _ in range(9)]`

## 2. 최댓값의 인덱스를 찾는 방법은?

나는 우선 max 함수를 통해 최댓값을 구하고, for문을 돌면서 list의 원소와 최댓값을 비교해 인덱스를 찾는 방법을 사용하였다. <br/>
그러나 파이썬에는 배열에서 값의 위치를 찾아주는 index 함수가 있다. 만약 중복된 값이 있으면 가장 최소의 위치를 리턴한다.
<br/>
만약 찾으려는 값이 86이라면
`list.index(86)` 로 간단하게 86의 인덱스를 찾을 수 있다.

<br/>

---

<br/>

# 기타 개념 정리

## str은 iterable 하다.

- str은 iterable 하기 때문에 map 함수의 인자로 넘겨서 처리할 수 있다.
- 예시
  ```python
  a = '1700'
  b = list(map(int, a))
  print(b)
  >> [1, 7, 0, 0]
  ```

## 리스트에서 특정 요소의 개수 구하기 (count)

- count 함수를 이용하면 리스트에서 특정 요소가 몇 개 있는지 구할 수 있다.
- 예를 들어, 위 예시에 이어서 b 리스트에서 0이 몇개인지 구하려면 `b.count(0)` 으로 구할 수 있다.
