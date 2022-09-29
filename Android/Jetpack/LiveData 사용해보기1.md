> ### 목차
>
> [1. LiveData에 대한 개요 / 간단한 예제](#livedata에-대한-개요--간단한-예제)
> [2. ViewModel과 LiveData 함께 써보기](#viewmodel과-livedata-함께-써보기)
> [3. LiveData와 MutableLiveData 차이](#livedata와-mutablelivedata-차이)

> ### LiveData에 대한 개요 / 간단한 예제

`LiveData`는 관찰 가능한 데이터 홀더 클래스이다. 수명주기를 인식한다.

- UI와 데이터 상태의 일치 보장
- 메모리 누수 없음
- 중지된 활동으로 인한 비정상 종료 없음
- 수명 주기를 더 이상 수동으로 처리하지 않음
- 최신 데이터 유지
- 적절한 구성 변경
- 리소스 공유

-> 데이터를 관찰해줄 수 있는 친구(LifeCycle과 결합해서)

LiveData를 활용해서, 버튼을 누르면 화면의 숫자가 1씩 증가하는 간단한 예제를 만들어봤다.
![](https://velog.velcdn.com/images/woonyumnyum/post/b911af93-492a-47e8-9eef-c6ab0033c5f6/image.png)

#### activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context=".MainActivity">

        <TextView
            android:id="@+id/textArea"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="0"
            android:textSize="60sp"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <Button
            android:id="@+id/plus"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="plus"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintStart_toStartOf="parent" />

        <Button
            android:id="@+id/minus"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="minus"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent" />

    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
```

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
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//LiveData
//데이터를 관찰해줄 수 있는 친구(LifeCycle과 결합해서)

class MainActivity : AppCompatActivity() {

	//LiveData 선언
    private var testMutableLiveData = MutableLiveData(0)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.plus).setOnClickListener {
            testMutableLiveData.value = testMutableLiveData.value!!.plus(1)
        }
        //데이터 변하는 것 관찰
        testMutableLiveData.observe(this, Observer {
            Log.d("MainActivity", testMutableLiveData.value.toString())
            findViewById<TextView>(R.id.textArea).text = testMutableLiveData.value.toString()
        })
    }
}
```

버튼을 클릭할 때마다 LiveData의 값을 1씩 증가시킨다. 값이 바뀔때마다 textView의 텍스트 설정은 observe 함수에서 해준다.
ovserve 함수는 LiveData의 값이 변하는 것을 관찰하는 함수이다. 로그를 찍어보니 데이터의 값이 변할때마다 로그가 잘 찍히는 것을 확인할 수 있다.
![](https://velog.velcdn.com/images/woonyumnyum/post/2a12be78-08f0-4d9c-abd9-5ab39a566f94/image.png)

> ### ViewModel과 LiveData 함께 써보기

이제 위의 예제를 ViewModel과 같이 써보자.

만약 지금보다 로직이 복잡해지면 모든 작업을 Activity에서 하면 너무 코드가 복잡해진다. 이럴 때 ViewModel로 로직을 빼서 사용하면 좋다.

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MainViewModel:ViewModel() {
    var testMutableLiveData = MutableLiveData(0)

    fun plusLiveDataValue(){
        testMutableLiveData.value = testMutableLiveData.value!!.plus(1)
    }
}
```

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
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//LiveData
//데이터를 관찰해줄 수 있는 친구(LifeCycle과 결합해서)

class MainActivity : AppCompatActivity() {

    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)

        findViewById<Button>(R.id.plus).setOnClickListener {
            viewModel.plusLiveDataValue()
        }
        //데이터 변하는 것 관찰
        viewModel.testMutableLiveData.observe(this, Observer {
            //findViewById<TextView>(R.id.textArea).text = viewModel.testMutableLiveData.value.toString()
            //아래 코드로 작성해도 된다.
            findViewById<TextView>(R.id.textArea).text = it.toString()
        })
    }
}
```

위의 예제와 달리, ViewModel을 사용했기 때문에 화면을 회전해도 값이 보존된다.

> ### LiveData와 MutableLiveData 차이

LiveData는 캡슐화를 위해 사용한다. 즉, ViewModel 안에서만 값을 변경하도록 하고싶을 때 사용한다.

지금까지 했던 코드를 LiveData를 이용해서 구현해보자.

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MainViewModel:ViewModel() {
    private var _testMutableLiveData = MutableLiveData(0)
    val testLiveData : LiveData<Int>
        get() = _testMutableLiveData

    fun plusLiveDataValue(){
        _testMutableLiveData.value = _testMutableLiveData.value!!.plus(1)
    }

}
```

#### MainAvtivity.kt

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
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//LiveData
//데이터를 관찰해줄 수 있는 친구(LifeCycle과 결합해서)

class MainActivity : AppCompatActivity() {

    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)

        findViewById<Button>(R.id.plus).setOnClickListener {
            viewModel.plusLiveDataValue()
        }
        //데이터 변하는 것 관찰
        viewModel.testLiveData.observe(this, Observer {
            findViewById<TextView>(R.id.textArea).text = viewModel.testLiveData.value.toString()
        })

         //액티비티에서 LiveData 값 변경 불가
        //viewModel.testLiveData.value = 30
    }
}
```

LiveData를 사용하면 이제 액티비티에서 값 수정은 불가능하다.
