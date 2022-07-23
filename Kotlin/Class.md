# 클래스

## 1. 클래스의 기본 구조

```kotlin
class 클래스명 {
    var 변수
    fun 함수(){
        //코드
    }
}
```

### 프로퍼티(property)

- 클래스 내부에 정의되는 변수입니다. 멤버 변수라고도 부릅니다.

### 메서드(method)

- 클래스 내부에 정의되는 함수입니다. 멤버 함수라고도 부릅니다.

## 2. 클래스의 생성

- 클래스를 사용할 때에는 생성자(constructor)를 호출해야지만 클래스가 생성됩니다.
- 코틀린의 클래스는 하나의 프라이머리 생성자(primary constructor)와 다수의 세컨더리 생성자(secondary constructor)를 가질 수 있습니다.

### 프라이머리 생성자

- 프라이머리 생성자는 클래스 헤더에 위치합니다. (클래스 이름 오른편)

```kotlin
class KotlinOne constructor(value:String){ /*...*/ }
```

- constructor 옆의 괄호가 프로퍼티의 선언과 초기화를 같이 해줍니다. 그래서 자바 코드에 비해 길이가 상당히 짧아집니다. (val/var이 없다면 프로퍼티를 초기화하는 식이나 초기화 블록(init 블록) 안에서만 프라이머리 생성자의 파라미터를 참조할 수 있습니다.)
- 생성자에 접근 제한자(public, private)이나 특정 옵션이 없다면 constructor 키워드를 생략할 수 있습니다.
- 프라이머리 생성자는 클래스 헤더에 위치하기 때문에 어떤 실행문도 포함할 수 없습니다. 만약 초기화하는 코드를 넣고 싶은 경우, init 블록으로 대체할 수 있습니다.
- init 블록에는 클래스의 객체가 만들어질 때 실행될 초기화 코드가 들어갑니다.
- 클래스의 생성자가 호출되면 init 블록의 코드가 실행되고, init 블록에서는 생성자를 통해 넘어온 파라미터에 접근할 수 있습니다.

```kotlin
class KotlinTwo(value:String){
    val firstProperty = "First Property : ${value}"

    init{
        Log.d("class", "생성자로부터 전달받은 값은 ${value}입니다.")
    }

    val secondProperty = "Second Property : ${value}"
}
```

- 프로퍼티를 초기화하는 식이나 초기화 블록(init 블록) 안에서만 주 생성자의 파라미터를 참조할 수 있습니다.
- 인스턴스 초기화를 할 때, init 블록과 property 선언 및 초기화는 같은 우선순위를 가져 위에서부터 선언된 순서대로 수행됩니다.
- 만약 추상클래스가 아닌 클래스가 어떠한 생성자도 선언하지 않았다면, 코틀린은 자동으로 아무런 파라미터가 없는 빈 코드 블록의 init 생성자를 호출합니다.

### 세컨더리 생성자

- 세컨더리 생성자는 constructor 키워드를 마치 함수처럼 사용해서 작성할 수 있습니다.
- 이때 프라이머리 생성자와 다르게 constructor 키워드는 생략할 수 없습니다.

```kotlin
class KotlinTwo{
    constructor (value:String) {
        Log.d("class", "생성자로부터 전달받은 값은 ${value}입니다.")
    }
}
```

- 만약 클래스에 프라이머리 생성자가 있을 경우 각 세컨더리 생성자들은 반드시 기본 생성자가 갖고 있는 파라미터들을 갖고 있어야 합니다. 그리고 무조건 this() 생성자를 이용해 직간접적으로 프라이머리 생성자에 생성을 위임해야 합니다.
- 예시

```kotlin
class Person(val name: String){
    var age: Int = 26
    constructor(name:String, age:Int): this(name){
        this.age = age
    }

    constructor(name:String, age:Int, height:Int): this(name, age){
        this.height = height
    }
}
```

- 위 코드에서 this(name)을 명시해주지 않는다면 컴파일 에러가 납니다.
- 만약 프라이머리 생성자, init 블럭, 세컨더리 생성자가 모두 있으면 어떻게 될까요?
  우선 우리는 init 블럭은 프라이머리 생성자의 일부라는 것을 알아야 합니다. 프라이머리 생성자는 세컨더리 생성자의 첫 번째 실행문으로 실행됩니다. 따라서 init 코드는 항상 세컨더리 생성자의 body 보다 먼저 실행됩니다.

## 3. 클래스의 사용

- 클래스의 이름에 괄호를 붙여서 클래스의 생성자를 호출합니다.
- 아무런 파라미터 없이 클래스를 호출하면 init 블록이 있는 생성자가 호출되면서 init 블록 안의 코드가 자동으로 실행됩니다. 세컨더리 생성자의 경우 constructor 블록 안의 코드가 실행됩니다.

```kotlin
var kotlin = Kotlin()
```

- 이와 같이 Kotlin 클래스의 생성자를 호출한 후 생성되는 것을 인스턴스(instance)라고 하는데, 생성된 인스턴스는 변수에 담아둘 수 있습니다.

### 클래스를 인스턴스화 하지 않고 사용하기 : companion object

- companion object 코드 블록을 사용하면 클래스를 생성자로 인스턴스화하지 않아도 블록 안의 프로퍼티와 메소드를 호출해서 사용할 수 있습니다.
- 예시

```kotlin
class KotlinFour{
    companion object{
        var one: String = "None"
        fun printOne(){
            Log.d("class", "one에 입력된 값은 ${one}입니다.")
        }
    }
}

KotlinFour.one = "새로운 값"
KotlinFour.printOne()
```

- 우리가 지금까지 사용한 Log 클래스의 메서드 d(), e()가 모두 companion object 코드 블록 안에 만들어져 있기 때문에 생성자 없이 바로 호출해서 사용할 수 있었습니다.

## 4. 클래스의 상속과 확장

### 상속은 왜 사용할까?

- 안드로이드에는 Activity라는 클래스가 미리 만들어져 있고, Activity 클래스 내부에는 여러 기능들이 미리 정의되어 있습니다. 상속이 있기 때문에 이 Activity 클래스를 상속받아 약간의 코드만 추가하면 간단한 앱을 만들 수 있습니다.

### 클래스의 상속

- 상속 대상이 되는 부모 클래스는 open 키워드로 만들어야만 자식 클래스에서 사용할 수 있습니다.
- 상속을 받을 자식 클래스에서는 클론을 이용해서 상속할 부모 클래스를 지정합니다.
- 클래스 상속은 부모의 생성자를 호출해서 생성된 인스턴스를 자식이 갖는 과정이기 때문에 부모 클래스명 다음에 괄호를 입력해서 생성자를 호출합니다.

```kotlin
open class 부모 클래스(value:String) { /*..*/ }
class 자식 클래스(value: Sring): 부모 클래스(value) { /*..*/ }
```

### 생성자 파라미터가 있는 클래스의 상속

- 위와 같이 상속될 부모 클래스의 생성자에 파라미터가 있다면 자식 클래스의 생성자를 통해 값을 전달할 수 있습니다.
- 부모 클래스에 세컨더리 생성자가 있다면, 자식 클래스의 세컨더리 생성자에서 super 키워드로 부모 클래스에 전달할 수 있습니다.
- 다음은 안드로이드의 View 클래스를 상속받는 예제입니다. 부모 클래스의 세컨더리 생성자를 이용하는 경우 부모 클래스명 다음에 오는 괄호를 생략합니다.

```kotlin
class CustomView:View(생략){
    constructor(ctx:Context): super(ctx)
    constructor(ctx:Context, attrs: AttributeSet): super(ctx, attrs)
}
```

### 프로퍼티와 메서드의 재정의 : 오버라이드

- 상속받은 부모 클래스의 프로퍼티와 메서드 중에 자식 클래스에서는 다른 용도로 사용해야하는 경우가 있습니다.
- 이런 경우 override 키워드를 사용해서 재정의할 수 있습니다.
- 오버라이드할 때는 프로퍼티나 메서드도 클래스처럼 앞에 open을 붙여서 상속할 준비가 되어 있어야 합니다.

```kotlin
open class BaseClass{
    open var opened: String = "I am"
    open fun opened() { /*..*/ }
    fun notOpened() { /*..*/ }
}

class ChildClass: BaseClass(){
    override var opened:String = "You are"
    override fun opened() { /*..*/ }
    //오버라이드 불가
    override fun notOpened() { /*..*/ }
}
```

## 5. 설계도구

### 추상화

- 프로그래밍을 하기 전 개념 설계 단계에서는 클래스의 이름과 클래스 안에 있음 직한 기능들을 유추해서 메서드 이름으로 먼저 나열합니다.
- 이때 명확한 코드는 설계 단계에서 메서드 블록 안에 직접 코딩하는데, 만약 앞으로 상속받을 자식 클래스의 특징에 따라 코드가 결정될 가능성이 있다면 해당 메서드의 이름만 작성합니다. 이것을 추상화라고 하며, abstract 키워드를 사용해서 명시합니다.
- 구현 단계에서는 이 추상화된 클래스를 상속받아서 아직 구현되지 않은 부분을 마저 구현합니다.
- 추상 클래스는 독립적으로 인스턴스화 할 수 없습니다.

```kotlin
abstract class Design{
    abstract fun drawText()
    abstract fun draw()
    fun showWindow(){ /*..*/ }
}

class Implements: Design(){
    override fun drawText(){ /*..*/ }
    override fun draw(){ /*..*/ }
}
```

### 인터페이스

- 인터페이스는 실행 코드 없이 메서드 이름만 가진 추상 클래스라고 생각해도 무방합니다.
- 즉, 개념 클래스 중에 실행 코드가 한 줄이라도 있으면 추상화, 코드 없이 메서드 이름만 나열되어 있으면 인터페이스 입니다.
- 인터페이스는 상속 관계의 설계보다는 외부 모듈에서 내가 만든 모듈을 사용할 수 있도록 메서드의 이름만 나열해둔 일종의 명세서로 제공됩니다.

```kotlin
interface 인터페이스명{
    var 변수: String
    fun 함수1()
    fun 함수2()
}

```

- 코틀린은 프로퍼티도 인터페이스 내부에 정의할 수 있는데, 대부분의 객체지향 언어에서는 지원하지 않습니다.
- 추상 클래스와 다르게 class 키워드는 사용되지 않습니다.
- 인터페이스의 프로퍼티와 메서드 앞에는 abstract 키워드가 생략된 형태입니다.

#### 클래스에서 구현하기

- 인터페이스를 클래스에서 구현할 때는 상속과는 다르게 생성자를 호출하지 않고 인터페이스 이름만 지정해주면 됩니다.

```kotlin
interface InterfaceKotlin{
    var variable: String
    fun get()
    fun set()
}

class KotlinImpl: InterfaceKotlin{
    override var variable: String = "init value"
    override fun get() { /*..*/ }
    override fun set() { /*..*/ }
}
```

- 인터페이스를 클래스의 상속 형태가 아닌 소스 코드에서 직접 구현할 때도 있는데, object 키워드를 사용해서 구현해야 합니다.

```kotlin
var kotlinImpl = object: InterfaceKotlin {
    override var variable: String = "init value"
    override fun get() { /*..*/ }
    override fun set() { /*..*/ }
}
```

- 인터페이스는 외부의 다른 모듈을 위한 의사소통 방식을 정의하는 것입니다. 혼자 개발할 때는 인터페이스를 사용하지 않는 것이 좋습니다. 남용하면 코드의 가독성과 구현 효율성이 떨어지기 때문입니다.
