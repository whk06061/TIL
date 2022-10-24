내용이 길어져 이전 글에 이어서 2탄 시작!

> ## 5. Nullable / NonNull

### ? 연산자

자바에서는 Null pointer Exception을 컴파일 시점(개발자가 코드를 작성할때 실시간으로)에서 잡지 못하고 런타임 시점에서 오류를 발생시켰다.

이는 굉장히 불편했기 때문에 코틀린에서는 컴파일 시점에서 null exception을 잡기 위해 물음표 연산자를 도입했다.

이 경우 name은 null 값이 될 수 없다.
타입을 생락하면 nonNull 타입이 된다.

```kotlin
var name: String = "joyce"
```

물음표만 붙여주면 nullable 타입이 되기 때문에 null 값을 넣을 수 있다.

```kotlin
var nullName: String? = null
```

그럼 null 체크는 어떻게 하는지 알아보자~
name은 toUpperCase 메서드를 바로 사용할 수 있다.
왜냐하면 name은 nonNull 타입이기 때문에 null 일리가 없기 때문이다.

```kotlin
var nameInUpperCase: String = name.toUpperCase()
```

Nullable 타입의 경우 우리가 물음표 연산자를 이용해 체크를 해줘야 한다.
nullName 뒤 물음표 연산자의 의미 : nullName이 not null이면 toUpperCase를 하고, null이면 `nullName?.toUpperCase()` 이 전체가 null을 반환한다. 그렇기 때문에 nullNameInUpperCase 변수도 nullable 타입이 된다.

```kotlin
var nullNameInUpperCase: String? = nullName?.toUpperCase()
```

### 엘비스 연산자 ?:

(구십도 돌려서 보면 엘비스의 머리와 닮았다고 이름이 엘비스 연산자라고 한다... 귀욤...)

위 예제에서 nullName이 null 이면 null을 반환한다고 했다. 근데 null이 아닌 다른 값을 반환하고 싶을 때 엘비스 연산자를 쓸 수 있다.

lastName이 null 이라면 "No lastName"을 반환한다.
(lastName이 not null이라면 lastName을 반환할 것이다.)

```kotlin
var name = "joyce"
val lastName: String? = null
val fullName = name + " " + (lastName?:"No lastName")
```

### !! 연산자

!! 연산자를 쓰면 Nullable 타입인 변수지만 Null 이 아니란 것을 개발자가 컴파일러에게 보증해 준다.

개발하면서 여기에는 Null이 들어갈리가 절대 없다고 생각될 때 !! 연산자를 씀으로써 컴파일러가 Null이 아니라고 생각할 수 있다.

mNotNull은 Null이 아님을 확인시켜줬으므로 그 아래 코드부터는 연산자 없이 변수를 그냥 쓸 수 있다.

```kotlin
fun ignoreNulls(str: String?){
	val mNotNull: String = str!!
    val upper = mNotNull.toUpperCase()
}
```

그러나 정말 확실하게 null이 아닐때가 아니면 사용을 지양해야한다. 괜히 에러가 날 수 있다..

### let 함수

email이 null이 아니면 let 함수를 실행하라는 의미이다.
let은 자신의 receiver 객체를(여기서는 email) 람다식 내부로 옮겨서 실행하는 구문이다.
email이 null이 아니라면 람다식 내부로 옮겨준다.(it 파라미터로 받아진다.)

email이 null 이라면 println은 실행되지 않기 때문에 굉장히 안전하다.

```kotlin
fun ignoreNulls(str: String?){
    val email: String? = "hoycehongxxxx@nana.vom"
    email?.let{
    	//email 대신 it을 써줘도 됨
    	println("my email is ${email}")
    }
}
```

> ## 6. 클래스

코틀린이 자바와 다른 점은 꼭 파일 이름과 클래스 이름이 일치하지 않아도 되며, 한 파일 안에 여러 클래스를 자유롭게 작성할 수 있다.

코틀린이 자바와 다른 또 다른 점은 클래스의 객체를 생성할 때 new 키워드가 필요없다.

```kotlin
class Person{

	val name = "joyce"

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}

fun main(){
	val human = Human()
    human.eatingCake()

    println("this human's name is ${human.name}")
}
```

### 생성자

자바에서는 클래스 이름과 똑같은 생성자 함수를 만들어서 초기화를 진행한다.
코틀린은 자바와 조금 다르다.

#### 기본 생성자(주 생성자)

기본 생성자는 아래와 같이 class 이름 옆에 constructor 함수를 이용해 매개변수를 받고 클래스 내부에서 프로퍼티에 할당해준다. 또는 constructor 함수 내에서 바로 프로퍼티에 할당해 줄 수도 있다.
(constructor 키워드는 생략 가능하다.)

```kotlin
/*class Person constructor(name: String){

	val name = name

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}*/

//위의 코드처럼 적는 것과 똑같음
class Person (val name: String){

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}

fun main(){
	val human = Human("minsu")
    human.eatingCake()

    println("this human's name is ${human.name}")
}
```

위의 코드에서 클래스의 객체를 생성할 때 값을 안넘겨주면 에러가 발생한다. 왜냐하면 name의 초기값이 없기 때문이다.
name 프로퍼티에 디폴트값을 설정해줄 수 있다. 디폴트 값을 부여하게 되면 빈 생성자와 파라미터가 있는 생성자 두 개를 만들기 때문에 객체를 생성할 때 값을 안넘겨줘도 무방하다. 왜냐하면 빈 생성자로 생성되고 name을 디폴트값으로 설정해준다.

```kotlin
class Person (val name: String = "Anonymous"){

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}
```

생성자에서 코드 블록을 넣고 싶으면 어떻게 해야할까?
그럴 땐 init 함수를 쓰면 된다.

#### init 함수

처음 인스턴스를 생성할 때 어떤 동작을 하고싶은지 적어줄 수 있다. init 함수도 주 생성자의 일부라서 constructor 함수가 (`val name: String = "Anonymous"`) 실행됨과 동시에 init 함수가 실행된다.

```kotlin
class Person (val name: String = "Anonymous"){

    init{
    	println("New human has been born!!")
    }

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}
```

#### 부 생성자

자바에서는 오버로딩을 통해 매개변수를 다르게 해서 생성자를 여러개 만들었다.
코틀린에서는 부 생성자를 (constructor 함수) 통해 다른 생성자를 만들 수 있다. (cf. 주 생성자의 위치는 클래스 이름 옆에 적거나, init 함수로 적는다.)
부 생성자는 this 키워드를 사용해서 반드시 주 생성자의 위임을 받아야 한다.
this 키워드를 사용해서 주 생성자로부터 name을 받아오면 자동으로 부 생성자의 name에 상속이 된다.

```kotlin
class Person (val name: String = "Anonymous"){

	constructor(name: String, age: Int): this(name){

    }

    init{
    	println("New human has been born!!")
    }

	fun eatingCake(){
    	println("This is so yummyyy~")
    }
}
```

한 가지 유의해야 될 점은 부생성자가 init 함수보다 위에 있지만 객체를 생성할 때 init 함수가 부 생성자보다 먼저 실행된다. 왜냐하면 init 함수는 주 생성자의 일부이기 때문에 constructor가 아무리 많이 있어도 init 함수가 먼저 실행된다.

### 상속

Human 클래스를 상속받아보자.
코틀린에서는 자바에서 사용하는 extends 대신 콜론 기호를 사용하면 된다.
코틀린 클래스는 final 클래스이기 때문에 아무리 같은 파일 내에 있어도 다른 클래스에 접근을 못한다. 그렇기 때문에 부모 클래스에 open 클래스를 붙여줘야 한다.
그리고 부모클래스에서 상속받은 메서드를 오버라이딩 해주려면 오버라이딩 하려는 부모의 메서드 앞에 open 키워드를 붙여줘야 한다.
그리고 super.메서드 하면 부모의 메서드도 사용할 수 있다.

```kotlin

open class Person (val name: String = "Anonymous"){

    //위와 동일하므로 생략

    open fun singASong(){
    	println("lalala")
    }
}

class Korean : Human(){

	override fun singASong(){
    	super.singASong()
    	println("랄랄라")
        println("My name is ${name}")
    }
}
```

만약 Korean 객체를 생성할 때 아무런 매개변수도 넘겨주지 않으면 부모인 Human의 생성자 중 파라미터가 없는 생성자에 의해 name에 "Anonymous"가 들어가게 된다.
그래서 아래 코드를 실행하면
"랄랄라"
"My name is Anonymous"
가 출력된다.

```kotlin
val korean = Korean()
korean.singASong()
```

그리고 자바와 똑같이 코틀린에서도 하나의 클래스밖에 상속받지 못한다.
