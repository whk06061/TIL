우테코 프리코스를 대비하여 코틀린 문법을 정리하려고 한다.
https://www.youtube.com/watch?v=IDVnZPjRCYg&t=75s
위 강의를 들으며 새로 배운 내용, 중요한 내용만 정리할 예정이다..!😊

> ## 1. 함수

### 실행의 시작점, main() 함수

![](https://velog.velcdn.com/images/woonyumnyum/post/c0e9d7ff-541e-48b5-919f-0e4f0e02b738/image.png)

**main() 함수는 최상위 함수로 실행 진입점이다.**
자바와 같은 객체지향언어는 프로그램을 실행하기 위해 클래스와 그 안에 main() 함수가 필요하다.
코틀린은 클래스 없이 main() 함수 하나로 실행 가능하다.

main 함수의 args 매개변수로 값을 넘겨줄 수도 있다.
Run > Edit Configurations 로 들어가서 Program arguments 항목에 명령형 인자를 지정하면 main 함수로 값이 전달된다.

> ## 2. 조건식

### if 조건식 간단하게 쓰기

두 수 중 더 큰 수를 반환하는 함수를 만들어보자.
기존에 쓰던 방법은 아래와 같다.

```kotlin
fun maxBy(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}
```

그러나 코틀린은 더 간단한 형식을 지원한다.
(코틀린은 삼항 연산자가 없기 때문에 이처럼 표현한다.)

```kotlin
fun maxBy(a: Int, b: Int): Int = if (a > b) a else b
```

### when 조건식

다른 언어의 switch 문법과 똑같다.

1. 기본 문법

```kotlin
fun checkNum(score: Int){
    when(score){
        0 -> println("This is 0")
        1 -> println("This is 0")
        2, 3 -> println("This is 2 or 3")
        else -> println("I don't know")
    }
}
```

복수 정답이 가능하고 어디에도 해당되지 않을 때에는 else로 빠진다.

2. return 식으로 쓸 수 있다.
   expression으로 쓸 때는 무조건 else를 써줘야 한다.

```kotlin
fun checkNum(score: Int) {

    val a = when (score) {
        1 -> 1
        2 -> 2
        else -> 100
    }
}
```

3. 범위를 쓸 수 있다.

```kotlin
fun checkNum(score: Int) {

    when (score) {
        in 90..100 -> print("You are genius")
        in 10..80 -> print("Not bad")
        else -> print("OK")
    }
}
```

> ## 3. Expression vs Statement

무슨 작업을 해서 **값을 반환하면**(값을 만들면) `expression` 이다.

expression 예시1>
a 또는 b 라는 값을 만들기 때문에 이때의 if문은 expression 으로 사용됐다.

```kotlin
fun maxBy(a: Int, b: Int): Int = if (a > b) a else b
```

expression 예시2>
1 or 2 or 100 이라는 값을 만들기 때문에 이때의 when은 expression 이다.

```kotlin
  val a = when (score) {
        1 -> 1
        2 -> 2
        else -> 100
    }
```

**값을 만들지 않고** 어떤 걸 **실행하도록** 만드는 문장은 `statement` 이다.

statement 예시1>
이때의 when은 실행을 하기 때문에 statement 이다.

```kotlin
fun checkNum(score: Int) {
    when (score) {
        0 -> println("This is 0")
        1 -> println("This is 0")
        2, 3 -> println("This is 2 or 3")
        else -> println("I don't know")
    }
}
```

#### kotlin vs java

참고로, 코틀린의 모든 함수는 `expression`이다.
아무것도 return 하지 않는 함수도 사실은 Unit을 return 한다.

코틀린과 달리 자바는 리턴값이 없는 void 함수가 존재하며, void 함수는 expression이 아니라 statement로 사용된다.

또한 자바에서는 if문이 statement로 밖에 사용되지 않았다면 코틀린에서는 expression 으로'도' 사용된다.

> ## 4. Array와 List

`Array`는 메모리가 처음에 할당되어 만들어지기 때문에 처음에 크기를 지정해줘야 한다.
Array는 수정이 가능한 Mutable 로 사이즈만 변경하지 않는다면 값의 변경은 가능하다.

`List`는 수정이 불가한 읽기전용인 List와 수정이 가능한 MutableList로 나뉜다.
MutableList의 가장 대표적인 것은 ArrayList이다.

<br/>

글이 길어져서 나머지는 2탄으로 ~.~

---

> 참고

- https://ddolcat.tistory.com/552
