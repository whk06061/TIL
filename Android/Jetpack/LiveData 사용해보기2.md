> ### 목차
>
> [1. Fragment LiveData / LifeCycleOwner](#fragment-livedata--lifecycleowner)

> ### Fragment LiveData / LifeCycleOwner

액티비티에서 뷰바인딩을 이용해서 버튼1을 누르면 Fragment1로 이동하고, 버튼2를 누르면 Fragment2로 이동하는 예제를 만들어보자.

![](https://velog.velcdn.com/images/woonyumnyum/post/5abfad99-6031-400d-9eae-458c5421542c/image.png)

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

//LiveData
//데이터를 관찰해줄 수 있는 친구(LifeCycle과 결합해서)

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    val manager = supportFragmentManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        binding.btn1.setOnClickListener {
            val transaction = manager.beginTransaction()
            val fragment1 = BlankFragment1()
            transaction.replace(R.id.frameArea, fragment1)
            transaction.addToBackStack(null)
            transaction.commit()
        }

        binding.btn2.setOnClickListener {
            val transaction = manager.beginTransaction()
            val fragment2 = BlankFragment2()
            transaction.replace(R.id.frameArea, fragment2)
            transaction.addToBackStack(null)
            transaction.commit()
        }
    }
}
```

#### BlankFragment1.kt

```kotlin
package com.woonyum.jetpack_ex

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

class BlankFragment1 : Fragment() {

    private val TAG = "BlankFragment1"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_blank1, container, false)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        Log.d(TAG, "onDestroyView")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy")
    }

}
```

#### BlankFragment2.kt

```kotlin
package com.woonyum.jetpack_ex

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

class BlankFragment2 : Fragment() {

    private val TAG = "BlankFragment2"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_blank2, container, false)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        Log.d(TAG, "onDestroyView")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "onDestroy")
    }

}
```

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

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical">

            <Button
                android:id="@+id/btn1"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="btn1" />

            <Button
                android:id="@+id/btn2"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="btn2" />

            <androidx.fragment.app.FragmentContainerView
                android:id="@+id/frameArea"
                android:name="com.woonyum.jetpack_ex.BlankFragment1"
                android:layout_width="match_parent"
                android:layout_height="match_parent" />
        </LinearLayout>


    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
```

#### fragment_blank1.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".BlankFragment1">

    <!-- TODO: Update blank fragment layout -->
    <TextView
        android:textSize="30sp"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:text="fragment1" />

</FrameLayout>
```

#### fragment_blank2.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".BlankFragment2">

    <!-- TODO: Update blank fragment layout -->
    <TextView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:textSize="30sp"
        android:text="fragment2" />

</FrameLayout>
```

Fragment를 이동하면서 Fragment의 파괴를 중심으로 LifeCycle을 살펴보자.
![](https://velog.velcdn.com/images/woonyumnyum/post/ccc399ae-86e7-494a-8b92-08ade11b90d0/image.png)

위부터 순서대로 버튼2 클릭 -> 버튼1 클릭 -> 버튼2 클릭 -> 뒤로가기 버튼 클릭 했을 때의 로그이다.
기존 프래그먼트가 다른 프래그먼트에 가려질때마다 View가 파괴된다.
뒤로가기 버튼을 누르면 Fragment가 파괴된다.

이처럼 Fragment의 LifyCycle과 View의 LifeCycle이 달라서 문제가 생기는 부분들이 있다. (프래그먼트는 뷰보다 오래 지속된다)
그래서 Fragment에서 ViewBinding을 사용시 뷰가 파괴될때 bindingClass를 정리해줘야한다. (onDestroyView 함수에서 bindingClass를 null로 만들기)

프래그먼트에서 LiveData를 사용할 때도 이런 문제들 때문에 액티비티와 다르게 사용해야 한다.
이제 프래그먼트에서 ViewBinding + LiveData를 사용해보자.
