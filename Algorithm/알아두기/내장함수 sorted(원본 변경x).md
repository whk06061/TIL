### sorted() 사용하기

내장 함수 sorted : sorted(iterable 객체) 로 사용하며, 오름차순으로 정렬된 결과를 반환한다. 즉, 원본은 바뀌지 않는다. sorted(iterable 객체, reverse = True)를 사용하면 내림차순으로 정렬한다.

### 정렬 기준 명시하기

리스트 [('홍길동', 35), ('이순신', 75), ('아무개', 50)]이 있을 때, 원소를 튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬하고자 한다면 다음과 같이 사용할 수 있다.

```python
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)

print(result)
# [('홍길동', 35), ('아무개', 50), ('이순신', 75)] 출력
```

### 참고. 람다식 사용하기

일반적인 add 함수를 람다식으로 바꿔서 사용해보자

```python
def add(a,b):
    return a+b
#일반적인 add() 메서드 사용
print(add(3,7))

#람다 표현식으로 구현한 add() 메서드
print((lambda a, b:a+b)(3,7))
#10출력
```
