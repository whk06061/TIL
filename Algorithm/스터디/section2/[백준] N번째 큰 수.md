백준 링크 : https://www.acmicpc.net/problem/2693

<내 코드>

```python
T = int(input())
for _ in range(T):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[2])
```

<다른 사람 코드>

```python
x = int(input())
for i in range(x):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])
```

내 코드와 비슷하지만 오름차순으로 정렬하고 뒤에서 세번째 원소를 출력하는 방법도 있다.

(참고로 맨 마지막 원소를 출력하려면 리스트의 길이를 활용하거나 nums[-1]을 해주면 된다.)

<복습>

```python
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[2])
```
