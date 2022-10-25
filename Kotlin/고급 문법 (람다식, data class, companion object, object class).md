https://www.youtube.com/watch?v=Q5noYbbc9uc&t=36s
위 강의를 보며 모르는 부분, 중요한 부분을 정리했다.

> ## 람다식

람다는 함수형 프로그래밍인 코틀린에서 핵심 개념이다.
람다식은 value 처럼 사용할 수 있는 익명 함수이다.

참고로 익명 함수는 아래 처럼 이름없이 정의되는 함수를 말한다. 변수에 할당해서 쓴다.

```kotlin
// 익명함수를 생성하여 greeting에 할당
val greeting = fun(){ println("Hello") }
// 익명함수 호출
greeting("chacha")
```

다시 돌아와서 람다식은 value 처럼 사용할 수 있는 익명 함수라고 했는데 이렇게 사용된다.

1. 메서드의 파라미터로 넘겨줄 수 있다.
2. return 값으로 사용할 수가 있다.

### 람다 기본 형식

람다의 기본 정의는 아래과 같다.

```kotlin
val lambdaName: Type = {parameterList -> codeBody}
```

제곱을 계산하는 람다식을 작성해서 아래와 같이 쓸 수 있다.
변수 타입에 파라미터와 리턴 타입을 명시해주든지 코드 블록에서 파라미터 타입을 명시해줘야 타입 추론이 가능하다.
(변수 타입을 명시해 줄 때에 파라미터에는 여러 값이 올 수 있기 때문에 파라미터 타입에는 반드시 괄호를 쳐줘야 한다. 리턴 타입에는 괄호를 안쳐줘도 된다.)

그리고 항상 람다에서는 마지막에 있는 코드가 리턴 값이 된다.

```kotlin
fun main(args: Array<String>) {
    println(square(3))
    println(nameAge("joyce", 99))
}

val square: (Int) -> (Int) = { number -> number * number }

val nameAge = { name: String, age: Int ->
    "my name is ${name} I'm ${age}"
}
```

### 확장함수

예제1.
a와 b가 String 클래스이기 때문에 String 클래스를 확장시켜서 만든 pizzaIsGreat 확장함수를 메서드로 사용할 수 있게 된다.
확장함수에서 this는 확장함수가 불러질 오브젝트를 가리킨다.

```kotlin
fun main(args: Array<String>) {
    val a = "joyce said"
    val b = "mac said"
    println(a.pizzaIsGreat()) // joyce said Pizza is the best! 출력
    println(b.pizzaIsGreat()) // mac said Pizza is the best! 출력
}

val pizzaIsGreat: String.() -> String = {
    this + "Pizza is the best!"
}
```

예제2.
파라미터가 딱 하나일 때는 it 예약어를 통해 이 파라미터를 이용할 수 있다.
`this`가 가리키는 것은 확장함수가 불러질 오브젝트이다.
`it`은 Int 파라미터를 가리킨다.

```kotlin
fun main(args: Array<String>) {
    println(extendString("hyegyeong", 23))
}

fun extendString(name: String, age: Int): String {
    val introduceMyself : String.(Int) -> String = {

        "I am ${this} and ${it} years old"
    }
    return name.introduceMyself(age)
}
```

### 람다를 표현하는 여러가지 방법

1. 파라미터로 넘기기

우리가 함수에 파라미터를 적을 때는 항상 어떤 타입인지 명시해줬다.

```kotlin
fun maxBy(a: Int)
```

마찬가지로 람다의 인풋 타입과 아웃풋 타입을 명시해줘야 한다.

```kotlin
fun invokeLambda(lambda: (Double) -> Boolean)
```

invokeLambda 함수의 파라미터로 람다식을 받고 함수의 반환값은 Boolean이다.
함수를 호출할 때는 변수에 람다식을 집어넣어서 그 변수를 전달하면 된다.
또는 중괄호를 이용해서 바로 전달해도 된다. 이때의 it은 딱 하나 들어가는 인풋 파라미터를 가리킨다.
그리고 어떤 함수의 마지막 파라미터가 람다식이면 중괄호 { } 부분을 소괄호 밖으로 뺄 수 있다.

```kotlin
fun main(args: Array<String>) {
    val lambda = {number:Double ->
        number == 4.3213
    }
    println(invokeLambda(lambda)) //false 출력
    println(invokeLambda { it == 4.3213 })
}

fun invokeLambda(lambda: (Double) -> Boolean): Boolean{
    return lambda(5.2343)
}
```

### 익명 내부 함수

예를 들어 setOnClickListener 메서드를 사용할때 이 함수의 매개변수로 OnClickListener 인터페이스 객체를 넣는 방식과 바로 람다식을 넣는 방식을 쓸 수 있다.

이때 람다식은 아무 경우에나 넣을 수 있는게 아니고 두 가지 경우에서 쓸 수 있다.

1. Kotlin interface가 아닌 java interface 여야 한다.
   (OnClickListener 는 java interface이다.)
2. 그 인터페이스는 단 하나의 메서드만 가져야 한다.

> ## data class

data class는 data를 담는 그릇이 되는 클래스이다.
바디를 작성할 필요가 없으며 클래스 이름 옆 생성자로 프로퍼티를 초기화해줄 수 있다.

```kotlin
data class Ticket(val companyName: String, val name: String, var data: String, var seatNumber: Int)

// toString(), hashCode(), equals(), copy() 자동으로 컴파일러가 만들어줌
//pojo class 역할

fun main() {
    val ticketA = Ticket("koreanAir", "hyegyeong", "2022-10-25", 14)
    print(ticketA) // Ticket(companyName=koreanAir, name=hyegyeong, data=2022-10-25, seatNumber=14) 출력
}
```

데이터 클래스는 바디를 적어주지 않아도 컴파일러가 자동으로 toString(), hashCode(), equals(), copy() 메서드를 만들어준다.
그래서 객체를 출력하면 보기 쉽게 객체의 내용이 출력 된다. (toString() 함수 자동 호출)

> ## companion object

companion object는 자바의 static 대신 사용된다.
정적인 메서드나 정적인 변수를 선언할 때 사용한다.

companion object는 private 프로퍼티나 메서드를 읽어올 수 있게끔 해준다.

```kotlin
class Book private constructor(val id: Int, val name: String) {

    companion object{
        fun create() = Book(0, "animal farm") //Book 객체 리턴
    }
}

fun main(){
    val book = Book.create()
}
```

companion object는 메서드 외에 프로퍼티도 가질 수 있고 이름도 가질 수 있다. 또한 상속 받는 것도 가능하다.

> ## object class

코틀린에서는 object 라는 클래스를 사용해서 싱클톤 패턴을 적용한 클래스를 만들 수 있다.
object class는 모든 앱을 실행할 때 객체가 딱 한번 만들어지는 클래스이다.
아래 예제에서 CarFactory는 Car를 생성할 때마다 만들어야 한다. 그런데 object class로 만들면 Car를 만들 때마다 새로운 CarFactory 객체를 만드는 것이 아니라 최초의 한번만 객체를 생성하고 다시는 생성하지 않는다. 그러므로 불필요하게 메모리가 사용되는 것을 막을 수 있다.

```kotlin
object CarFactory {
    val cars = mutableListOf<Car>()
    fun makeCar(horsePower: Int):Car{
        val car = Car(horsePower)
        cars.add(car)
        return car
    }
}

data class Car(val horsePower: Int)

fun main(){
    val car = CarFactory.makeCar(10)
    val car2 = CarFactory.makeCar(100)
}
```

CarFactory는 한번 객체를 생성하고 계속 그 객체를 쓰기 때문에 일반 class 처럼 객체 생성문을 쓰지 않고 바로 객체로 사용한다. CarFactory는 이제 어디서 사용되든 처음 컴파일될 때의 인스턴스 딱 하나이다.

> 참고

- https://codechacha.com/ko/kotlin-lambda-expressions/
- https://kkangsnote.tistory.com/64
- https://blog.yena.io/studynote/2017/11/22/Kotlin-Lambda.html
