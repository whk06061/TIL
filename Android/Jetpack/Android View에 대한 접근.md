> ### 목차
>
> [1. ViewBinding과 DataBinding을 사용하는 이유](#viewbinding과-databinding을-사용하는-이유)
> [2. ViewBinding 사용하기](#viewbinding-사용하기)
> [3. DataBinding 사용하기](#databinding-사용하기)
> [3-1. DataBinding과 data class](#databinding과-data-class)

> ### ViewBinding과 DataBinding을 사용하는 이유

- 뷰에 접근할때마다 findViewById를 사용할 필요가 없다.
- `Null Safety` : 뷰를 직접 참조하기 때문에 없는 아이디로 인한 null exception 발생하지 않음.
- `Type Safety`: 뷰 타입이 일치하기 때문에 클래스 변환 예외가 발생할 위험이 없다. (ex. textView 인데 imageView라고 잘못 적어서 class cast exception이 발생할 위험이 없다.)

> ### ViewBinding 사용하기

#### 특징

- `ViewBinding`을 사용하면 뷰와 상호작용하는 코드를 쉽게 작성할 수 있다. (간단하게 작성할 수 있다는 것이 큰 장점)
- ViewBinding은 각 모듈 별로 설정된다. 모듈에 설정이 되면 각 XML 레이아웃 파일의 결합 클래스를 생성한다. (MainActivity의 경우 ActivityMainBinding 이라는 Binding Class 생성)(카멜 표기법에 따라 네이밍)
- Binding Class의 인스턴스는 ID를 가지고 있는 모든 뷰에 대한 직접 참조를 생성한다.

#### DataBinding과 비교

둘 다 뷰를 직접 참조하는데 사용할 수 있는 binding class를 제공한다.
뷰 바인딩은 보다 단순한 처리의 경우 적합하다.
<장점>

- 더 빠른 컴파일 : 주석을 처리할 필요 없음.
- 사용 편의성 : 뷰 바인딩에는 tag처리된 xml 레이아웃 파일이 필요하지 않아서 더 신속하다. 모듈에서 binding 사용 설정만으로 자동으로 모든 레이아웃의 binding class가 자동으로 생성된다.

<단점>

- layout 표현식 또는 변수를 지원하지 않으므로(xml 파일에서 layout 루트 태그로 감싸고 data 요소 및 view 요소를 적는 등..의 표현식 지원X) xml 레이아웃 파일에서 직접 동적 UI 콘텐츠를 선언하지 못한다.
- 양방향 데이터 결합을 지원하지 않는다.

#### build.gradle

```kotlin
buildFeatures{
		viewBinding = true
}
```

#### MainActivity.kt

```kotlin
// https://developer.android.com/topic/libraries/view-binding?hl=ko

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
		setContentView(view)

        binding.testText.text= "이거는 변경된 텍스트"
        binding.testText.setOnClickListener{
			val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)
		}

	}
}
```

#### activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/testText"
        android:textSize="50sp"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

#### SecondActivity.kt

```kotlin
class SecondActivity : AppCompatActivity() {

    val manager =supportFragmentManager

				override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        val transaction = manager.beginTransaction()
        val fragment = TestFragment()
        transaction.replace(R.id.frameArea, fragment)
        transaction.addToBackStack(null)
        transaction.commit()


    }

}
```

#### activity_second.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SecondActivity">

    <FrameLayout
        android:id="@+id/frameArea"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        />

</androidx.constraintlayout.widget.ConstraintLayout>
```

#### TestFragment.kt

```kotlin
class TestFragment : Fragment() {

    private var _binding : FragmentTestBinding? = null
    private val binding get() = _binding!!

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?,
    ): View? {

        _binding = FragmentTestBinding.inflate(inflater, container, false)
        val view = binding.root

		binding.fragmentText.text= "이거는 framgent Text"

        return view
    }


}
```

#### fragment_test.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".TestFragment">

    <!--TODO: Update blank fragment layout-->
    <TextView
        android:id="@+id/fragmentText"
        android:textSize="50sp"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:text="@string/hello_blank_fragment" />

</FrameLayout>
```

> ### DataBinding 사용하기

#### DataBinding 라이브러리

DataBinding 라이브러리는 UI 요소와 데이터를 프로그래밍적 방식으로 연결하지 않고 선언적 방식으로 결합할 수 있게 도와주는 라이브러리이다.

기존 프로그래밍적 방식으로는 아래와 같이 작성한다.

```kotlin
findViewById<TextView>(R.id.sample_text).apply {
        text = viewModel.userName
    }
```

그러나 DataBinding을 이용하면 레이아웃 파일에서 직접 위젯에 텍스트를 할당할 수 있다. 즉, 코틀린/자바 코드를 직접 호출하지 않아도 된다.

```xml
<TextView
        android:text="@{viewmodel.userName}" />
```

#### 특징

- RecyclerView에 각각의 item을 set해주는 작업도 자동으로 진행된다.
- data가 바뀌면 자동으로 View를 변경하게 할 수 있다.

#### build.gradle

```kotlin
buildFeatures{
	dataBinding = true
}
```

#### MainActivity.kt

```kotlin
// DataBinding
// ViewBinding 이랑 뭐가 다른가?
// 이름처럼 데이터를 연결해주는 역할을 할 수 있습니다. (데이터와 같이 결합해서 사용할 수 있음)
// DataBinding + LiveData

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)

        binding.dataBindingEx.text= "바뀐 텍스트"
        binding.dataBindingEx.setOnClickListener{
			val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)
		}

	}
}
```

#### activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity">

        <TextView
            android:id="@+id/dataBindingEx"
            android:textSize="50sp"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Hello World!"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

    </androidx.constraintlayout.widget.ConstraintLayout>

</layout>
```

#### SecondActivity.kt

```kotlin
class SecondActivity : AppCompatActivity() {

    val manager =supportFragmentManager

override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        val transaction = manager.beginTransaction()
        val fragment = TestFragment()
        transaction.replace(R.id.frameArea, fragment)
        transaction.addToBackStack(null)
        transaction.commit()

    }

}
```

#### activity_second.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SecondActivity">

    <FrameLayout
        android:id="@+id/frameArea"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</androidx.constraintlayout.widget.ConstraintLayout>
```

#### TestFragment.kt

```kotlin
class TestFragment : Fragment() {

    lateinit var binding : FragmentTestBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?, ): View? {


        binding = DataBindingUtil.inflate(inflater, R.layout.fragment_test, container, false)

        binding.fragmentText.text= "변경된 텍스트"

        return binding.root
}


}
```

#### fragment_test.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".TestFragment">

        <!--TODO: Update blank fragment layout-->
        <TextView
            android:id="@+id/fragmentText"
            android:textSize="50sp"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:text="@string/hello_blank_fragment" />

    </FrameLayout>
</layout>
```

> ### DataBinding과 data class

data 객체를 view와 bind해서 사용해보자.

view에 보여줄 Person이라는 data class를 선언한다.

#### Person.kt

```kotlin
data class Person (
    val name : String,
    val age : Int
)
```

Person 객체를 초기화하여 xml 파일에서 선언된 data에 set해준다.

#### MainActivity.kt

```kotlin
// DataBinding
// 이름처럼, 뭔가 데이터를 어쩌고 저쩌고 해줄 수 없을까?(연결)
// 데이터 결합

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding

    var testCount = 20

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)

        // 기존의 방법
        // binding.test.text = "바뀐 텍스트"

        // 데이터 결합
        val person = Person("개복치", 20)
        binding.person= person
    }

    fun myClick(view : View) {
        Log.d("MainActivity", "onClick")
        testCount++

        val person = Person("개복치", testCount)
        binding.person= person

    }
}
```

`<data>` 태그는 `<layout>`에서 사용할 변수를 정의하는데 사용된다.
나는 Person 이라는 data class 객체를 사용할 것이기 때문에 name이 person인 변수를 한개 선언해주었다.
레이아웃 내의 표현식은 `"@{}"` 구문을 사용하여 작성한다.

#### activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <data>
        <variable
            name="person"
            type="com.bokchi.jetpack_ex.Person" />
    </data>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".MainActivity"
        android:orientation="vertical">

        <TextView
            android:id="@+id/test"
            android:textSize="100dp"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{person.name}"
            />

        <TextView
            android:textSize="100dp"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{Integer.toString(person.age)}"
            />

        <TextView
            android:textSize="100dp"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{person.age > 30 ? `나이 많음` : `나이 적음`}"
            />

        <Button
            android:text="btn"
            android:onClick="myClick"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"/>

    </LinearLayout>

</layout>
```
