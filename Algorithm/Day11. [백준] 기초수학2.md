# 알고리즘 공부 11일차

### 백준 문제 :

4948(시간초과), 9020

---

# 주요 문제 정리

## 4948. 베르트랑 공준

<br/>

> ### [문제](https://www.acmicpc.net/problem/4948)

#### <br/>베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.<br/>이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.<br/>예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)<br/>자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

<br/>

> ### Python3 코드

```python
N = 123456
sosoo_list = [False] * (N*2+1)

# 2 * N 까지의 모든 소수 구하기
for i in range(2,N*2+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosoo_list[i] = True

# 입력받은 수 범위에서 소수 개수 구하기
while True:
    result = 0
    input_n = int(input())
    if input_n == 0:
        break
    for i in range(input_n+1, 2*input_n+1):
        if sosoo_list[i] == True:
            result += 1
    print(result)
```

<br/>

> ### Python3 코드 풀이

### 1. 문제 요약

이 문제는 자연수 n을 입력받아 n보다 크고 2n보다 작은 소수의 개수를 구하는 문제이다.
<br/>

처음에는 n부터 2n까지 for문을 돌면서 소수인지 아닌지 일일이 계산을 해줬었는데 시간초과가 떠서 실패했다. 시간을 절약하려면 미리 입력 최대치인 123456까지의 소수를 미리 구한 후 입력 받은 범위 내에서 소수가 몇개가 있나 구해줘야한다.

### 2. 변수 설명

```python
N = 123456
sosoo_list = [False] * (N*2+1)
```

변수 N에는 입력 최대치인 123456을 넣어준다.
sosoo_list는 입력 범위까지의 모든 소수를 구하기 위한 리스트로, 소수인 인덱스에만 True가 저장된다.
(참고로, 리스트의 크기가 N\*2+1인 이유는 2N보다 작거나 같은 소수를 구해야하기 때문이고, 만약 1을 더해주지 않는다면 인덱스는 2\*N-1 번 까지밖에 만들어지지 않기 때문에 1을 더해줘야 한다.)

### 3. 미리 입력 범위까지의 모든 소수를 구해준다

```python
for i in range(2,N*2+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosoo_list[i] = True
```

외부 for문은 2부터 N\*2 사이의 모든 소수를 구해주기 위해 범위를 지정해준다.
내부 for문은 시간 절약을 위해 어떤 수의 제곱근 범위 안에 모든 약수가 존재한다는 성질을 이용해서 소수를 구해준다. (Day10 글 참고)
<br/>내부 for문을 모두 돌았는데 i가 j로 나누어떨어지지 않는다면 else문 안의 코드가 실행되며, 그때 i는 소수이기 때문에 해당 인덱스 값을 True로 바꿔준다.

### 4. 입력받은 범위에서 소수의 개수 구하기

```python
while True:
    result = 0
    input_n = int(input())
    if input_n == 0:
        break
    for i in range(input_n+1, 2*input_n+1):
        if sosoo_list[i] == True:
            result += 1
    print(result)

```

4번째 줄은 무한 for문을 돌면서 n을 입력받다가 0이 입력되면 프로그램을 종료시키는 코드이다.
for문은 입력받은 범위만큼 반복을 돌면서 해당 숫자가 만약 앞서 구한 리스트에서 소수로 판명이 났으면 result를 1 증가시키고 반복문을 다 돌면 result를 출력한다.

---

## 9020. 골드바흐의 추측

<br/>

> ### [문제](https://www.acmicpc.net/problem/9020)

#### <br/>1보다 큰 자연수 중에서 1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.<br/>골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.<br/>2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

<br/>

> ### Python3 코드

```python
import sys

N = 10000
sosoo_list = []
for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j  == 0 :
            break
    else:
        sosoo_list.append(i)

input_n = int(input())
for _ in range(input_n):
    even_number = int(sys.stdin.readline())
    # 짝수를 반으로 나눈 값을 기준으로 함
    pivot = even_number // 2
    # 반으로 나눈 값이 소수라면 바로 정답 출력
    if pivot in sosoo_list:
        print(f'{pivot} {pivot}')
    # 아니라면 구해줘야 함
    else:
        while True:
            # pivot이 소수가 될 때 까지 1을 빼줌
            if pivot in sosoo_list:
                # pivot 말고 나머지 값도 소수라면 답 출력
                if (even_number - pivot) in sosoo_list:
                    print(f'{pivot} {even_number-pivot}')
                    break
                # 아니라면 pivot을 더 작은 소수로 바꿔줌
                else:
                    pivot_index = sosoo_list.index(pivot)
                    pivot = sosoo_list[pivot_index-1]
            else:
                pivot -= 1
```

<br/>

> ### Python3 코드 풀이

### 1. 문제 요약

이 문제는 입력받은 짝수를 가장 근접한 두 소수의 합으로 표현할 때 그 두 소수를 출력하는 문제이다 .
<br/>

우선 각 짝수가 어떤 소수로 이루어져 있는지 구해봤다. 4 = [2, 2], 6 = [3, 3], 8 = [3, 5], 10 = [5, 5], 12 = [5, 7] 이렇게 나타낼 수 있다. 그리고 모든 짝수는 반으로 나눈 수와 가까운 소수의 합으로 이루어져 있다는 것을 알게되었다. 그래서 우선 입력 제한인 10000 까지의 모든 소수를 구한 다음, 입력받은 짝수를 반으로 나눈 수를 기준으로 그 수와 최대한 가까운 두 소수를 구해줬다.

### 2. 변수 설명

```python
N = 10000
sosoo_list = []
```

변수 N에는 입력 최대치인 10000을 넣어준다.
sosoo_list는 10000 까지의 모든 소수를 저장할 리스트이다.

### 3. 입력 범위까지의 모든 소수를 구해준다

```python
for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j  == 0 :
            break
    else:
        sosoo_list.append(i)
```

이 과정은 앞의 문제와 비슷하다.
외부 for문은 2부터 10000 사이의 모든 소수를 구해주기 위해 범위를 지정해준다.
내부 for문에서는 소수인지 아닌지 계산하여 소수라면 리스트에 추가해준다.

### 4. 짝수를 나타낼 수 있는 두 소수 구하기

```python
input_n = int(input())
for _ in range(input_n):
    even_number = int(sys.stdin.readline())
    # 짝수를 반으로 나눈 값을 기준으로 함
    pivot = even_number // 2
    # 반으로 나눈 값이 소수라면 바로 정답 출력
    if pivot in sosoo_list:
        print(f'{pivot} {pivot}')
    # 아니라면 구해줘야 함
    else:
        while True:
            # pivot이 소수가 될 때 까지 1을 빼줌
            if pivot in sosoo_list:
                # pivot 말고 나머지 값도 소수라면 답 출력
                if (even_number - pivot) in sosoo_list:
                    print(f'{pivot} {even_number-pivot}')
                    break
                # 아니라면 pivot을 더 작은 소수로 바꿔줌
                else:
                    pivot_index = sosoo_list.index(pivot)
                    pivot = sosoo_list[pivot_index-1]
            else:
                pivot -= 1
```

우선 짝수를 입력받아 even_number 변수에 넣는다. <br/>그리고 짝수를 반으로 나눈 값을 기준으로 삼기 위해 pivot 변수에 넣어준다.
<br/>
만약 pivot이 소수라면 바로 답을 출력해준다.
<br/>

pivot이 소수가 아니라면 이제 10번째 줄의 else 문으로 이동한다.
<br/>무한 while문을 돌면서 pivot이 소수가 될 때 까지 1을 빼준다.
<br/>

만약 pivot이 소수가 됐다면, 이제 even_number에서 pivot을 뺀 수도 소수인지 검사해준다.
<br/>소수라면 답을 출력해주고 while문을 벗어난다.
<br/>소수가 아니라면 현재 pivot보다 작은 최대의 소수로 pivot을 대체해준다. 이 과정은 even_number에서 새로운 pivot을 뺀 값이 소수가 될 때 까지 반복해준다.
