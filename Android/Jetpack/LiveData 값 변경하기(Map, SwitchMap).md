> ### 목차
>
> [1. Map, SwitchMap 이란?](#map-switchmap-이란)
> [2. 예제1](#예제1)
> [3. 예제2(LiveData + DataBinding + ViewModel)](#예제2livedata--databinding--viewmodel)

> ### [Map, SwitchMap 이란?](https://wooooooak.github.io/android/2019/07/13/liveData%EB%B3%80%ED%98%95%ED%95%98%EA%B8%B0/)

### Transformations

- Transformations는 LiveData를 위해 제공하는 클래스이다.
  Transformations 클래스를 이용하면 기존에 선언해두었던 LiveData를 변형해서 사용할 수 있다.

### Transformations.map

Transformations.map을 사용하기 전에 일반 배열에서의 map 예제를 살펴보자.

```kotlin
val list1 = listOf(1, 2, 3)
val list2 = list1.map{ it.times(2)}
print(list2) // [2, 4, 6]
```

코틀린 컬렉션에서 제공하는 map 함수를 이용하면 각각의 원소에 2를 곱한 새로운 리스트를 반환한다. 여기서 포인트는 **새로운 리스트**를 반환한다는 점이다.

`Transformations.map` 또한 마찬가지이다.

```kotlin
val userLiveData: MutableLiveData<User> = repository.getUser(id)
//마지막 인자가 람다식인 경우 소괄호 바깥으로 분리가능
val userNameLiveData: LiveData<String> = Transformations.map(userLiveData) { user ->
    user.firstName + " " + user.lastName
}
```

**map의 첫번째 인자**로 LiveData source를 넘겨준다. 이 LiveData source가 변경될 때마다 map이 반환하는 새로운 LiveData의 value역시 새롭게 갱신된다.

**두번째 인자**로 함수를 넘겨준다. 함수의 파라미터 타입은 source로 넘겨준 LiveData의 value 타입이며 함수의 return 값은 어떤 값이든 상관없다.

**Transformations.map의 return값은**(람다의 결과물말고) LiveData이다.
기존 컬렉션의 map 함수가 그랬듯이 Transformations.map 함수 역시 내용물 요소의 값만 변환시킬 뿐 LiveData를 리턴한다.

위의 예제에서 userNameLiveData의 value는 userLiveData의 value가 바뀔 때 마다 함께 갱신된다.

### Transformations.switchMap

```kotlin
 val userIdLiveData: MutableLiveData<Int> = MutableLiveData<Int>().apply { value = 1 };
 //마지막 인자가 람다식인 경우 소괄호 바깥으로 분리가능
 val userLiveData: LiveData<User> = Transformations.switchMap(userIdLiveData) { id ->
     repository.getUserById(id)
 }
```

**switchMap의 첫 번째 인자**로 LiveData source를 넘겨준다. 넘겨준 LiveData source 가 변경될 때마다 switchMap이 반환하는 새로운 LiveData의 value역시 새롭게 갱신된다.

**두 번째 인자**로는 함수를 넘겨준다. 함수의 파라미터 타입은 source로 넘겨준 LiveData의 value Type(여기서는 Int)이며 함수의 return값은 `LiveData`이어야만 한다.

`map과 다른점`은 람다 함수의 return값이 LiveData여야 한다는 것이다.
map의 경우 람다함수의 return값이 각 요소의 값들을 변경시키는 것에 불과하며 자동으로 LiveData가 되어서 결과물이 반환되었지만, switchMap의 경우 실제로 LiveData 하나를 반환해야 한다.
그래서 switchMap은 Model단이나 Room데이터베이스와 같이 애초에 LiveData를 반환하는 기능들과 자주 함께 쓰인다.

userLiveData의 value역시 userIdLiveData의 value가 바뀌면 자동으로 갱신되는데 map과 마찬가지로 내부적으로 MediatorLiveData가 사용되기 때문이다.

> ### 예제1

Map과 SwitchMap을 이용해서 LiveData의 값을 변경하는 예제를 만들어보자.
만약 10이 입력되면 첫번째 줄에는 10+10이, 두번째 줄에는 10\*10이 출력되는 예제를 만들어보자.
![](https://velog.velcdn.com/images/woonyumnyum/post/8146c911-74d5-4a86-9543-7168a2dfde25/image.png)

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.databinding.DataBindingUtil
import androidx.fragment.app.FragmentManager
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//LiveData Transformations

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)

        viewModel.liveCount.observe(this, Observer {
//            binding.resultArea1.text = (it+it).toString()
//            binding.resultArea2.text = (it * it).toString()
        })

        viewModel.mapLiveData.observe(this, Observer {
            binding.resultArea1.text = it.toString()
        })

        viewModel.switchMapLiveData.observe(this, Observer {
            binding.resultArea2.text = it.toString()
        })

        binding.btnArea.setOnClickListener {
            val count = binding.inputArea.text.toString().toInt()
            viewModel.setLiveDataValue(count)
        }
    }
}
```

주석처리한 코드처럼 Activity의 observer에서 데이터의 값을 계산해서 출력할 수도 있지만, 코드가 복잡해지기 때문에 ViewModel에서 Transformations.map/switchMap을 이용해서 데이터의 값을 변경했다.
그리고 LiveData를 사용했기 때문에 값이 갱신되면 observe함수로 감지하여 뷰를 갱신해주었다.

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Transformations
import androidx.lifecycle.ViewModel

class MainViewModel : ViewModel() {

    //Transformation -> map / switchMap

    //map -> 값을 return

    private var _mutableCount = MutableLiveData(0)
    val liveCount: LiveData<Int>
        get() = _mutableCount

    val mapLiveData = Transformations.map(liveCount) {
        it + it
    }

    val switchMapLiveData = Transformations.switchMap(liveCount){
        changeValue(it)
    }

    fun setLiveDataValue(count: Int) {
        _mutableCount.value = count
    }

    fun changeValue(count: Int): MutableLiveData<Int> {
        val testLiveData = MutableLiveData(count * count)
        return testLiveData
    }
}
```

ViewModel에서 LiveData의 값을 수정하는 방법은 `Map`을 이용하거나 `SwitchMap`을 이용하면 된다.
두 함수 모두 LiveData를 리턴한다.

> ### 예제2(LiveData + DataBinding + ViewModel)

DataBinding을 이용해서 LiveData를 변경하는 예제를 만들어보자.
next 버튼을 누를때마다 랜덤으로 과일이름과 뒤섞인 과일이름을 화면에 띄워준다.
![](https://velog.velcdn.com/images/woonyumnyum/post/7fe81eff-da7e-41c0-900d-6279e76f2289/image.png)
![](https://velog.velcdn.com/images/woonyumnyum/post/d2c8f136-62ec-4582-a49b-d20a9c17cfe8/image.png)

#### TestData.kt

```kotlin
package com.woonyum.jetpack_ex

val testDataList: List<String> = listOf(
    "apple",
    "strawberry",
    "pineapple",
    "peach",
    "grape",
    "melon",
    "mango"
)
```

랜덤으로 선택될 과일이름 리스트를 만들어준다.

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Transformations
import androidx.lifecycle.ViewModel

class MainViewModel:ViewModel() {

    private var _mutableWord = MutableLiveData("")
    val liveWord : LiveData<String>
    get() = _mutableWord

    private var _randomMutableWord = MutableLiveData("")
    val randomLiveWord : LiveData<String>
        get() = _randomMutableWord

    val newData = Transformations.switchMap(liveWord){
        shuffleRandomWord(it)
    }

    init{
        getNextData()
    }

    fun getNextData(){
        val currentWord = testDataList.random()
        val randomWord = currentWord.toCharArray()
        randomWord.shuffle()
        _mutableWord.value = currentWord
        _randomMutableWord.value = String(randomWord)
    }

    fun shuffleRandomWord(word:String):MutableLiveData<String>{
        val liveData = MutableLiveData("")
        val randomTextWord = word.toCharArray()
        randomTextWord.shuffle()
        liveData.value = String(randomTextWord)
        return liveData
    }
}
```

앱이 시작되자마자 데이터를 불러오기위해 init 함수에서 getNextData()함수를 호출해준다.
getNextData()함수에서는 현재 단어와 알파벳이 뒤섞인 단어를 만들어준다.
세번째 textView에 들어갈 값은 Transformations.switchMap 함수를 이용해서 LiveData를 변형해준다.

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//LiveData + DataBinding + ViewModel

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)
        binding.vm = viewModel
        binding.lifecycleOwner = this
        binding.next.setOnClickListener {
            viewModel.getNextData()
        }
    }
}
```

#### activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <data>

        <variable
            name="vm"
            type="com.woonyum.jetpack_ex.MainViewModel" />
    </data>

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context=".MainActivity">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@{vm.liveWord}"
                android:textSize="40sp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@{vm.randomLiveWord}"
                android:textSize="40sp" />

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@{vm.newData}"
                android:textSize="40sp" />

            <Button
                android:id="@+id/next"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="next" />

        </LinearLayout>

    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
```

MainActivity에서 observe 함수를 사용하는 대신, DataBinding을 사용해서 xml 안에서 바로 뷰에 데이터를 붙여주었다.
LiveData를 사용하였기 때문에 값이 갱신되면 실시간으로 뷰에 갱신되어 적용된다.
