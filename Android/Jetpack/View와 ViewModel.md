> ### 목차

---

[1. ViewModel 이란?](#viewmodel-이란)
[2. Activity에서 ViewModel 사용하기](#activity에서-viewmodel-사용하기)
[3. Fragment에서 ViewModel 사용하기](#fragment에서-viewmodel-사용하기)
[4. Activity / Fragment의 ViewModel 공유](#activity--fragment의-viewmodel-공유)
[5. ViewModel Factory](#viewmodel-factory)

> ### ViewModel 이란?

- ViewModel 클래스는 수명 주기를 고려하여 UI 관련 데이터를 저장하고 관리하도록 설계되었다.
- 화면 회전과 같이 구성을 변경할 때도 데이터를 유지할 수 있다.

<span style="color:#B9B9B9">_ViewModel 말고 기존의 onSaveInstanceState() 를 이용해서도 데이터를 관리할 수 있지만 이는 소량의 데이터에만 적합하다. _</span>

화면을 회전시키면 액티비티가 destroy되고 다시 create되기 때문에 기존 데이터가 초기화되는 문제가 생겨버린다.

이러한 문제를 방지하기 위해 안드로이드의 생명주기(LifeCycle)의 상태가 변경될 때마다 데이터를 잘 관리해줘야 하는데 ViewModel을 사용하면 이를 편리하게 관리할 수 있다.

또한 UI 컨트롤러(Activity, Fragment)에서 모든 것을 다 처리하려고 하면 복잡해지지만 ViewModel을 사용하면 테스트나 관리가 용이해진다.

---

> ### Activity에서 ViewModel 사용하기

+/- 버튼을 누를때마다 화면 속 숫자가 1씩 증감하는 간단한 기능을 만들었다.
![](https://velog.velcdn.com/images/woonyumnyum/post/b2e04380-e8ed-4093-b0a2-76f21f5d23b7/image.png)

만약 ViewModel을 사용하지 않으면 위에서 말했듯이 화면을 회전시킬 때마다 기존에 계산했던 값이 없어지고 0으로 초기화되는 문제가 발생한다. 이 문제를 ViewModel 클래스를 이용해서 수정해보았다.

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.ViewModel

//보통 ViewModel을 쓸때 아래와 같이 변수 하나만 만들어서 사용하지는 않고 LiveData 등등을 이용해서 함께 씀
//아래는 예제니까 그냥 참고만

class MainViewModel : ViewModel(){

    var countValue = 0

    fun plus(){
        countValue++
    }

    fun minus(){
        countValue--
    }
    fun getCount():Int{
        return countValue
    }
}
```

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.lifecycle.ViewModelProvider

class MainActivity : AppCompatActivity() {

//    private var countValue = 0

    lateinit var viewModel:MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)

        val plus_btn : Button = findViewById(R.id.btn_plus)
        val minus_btn : Button = findViewById(R.id.btn_minus)
        val result_tv : TextView = findViewById(R.id.tv_result)

        result_tv.text = viewModel.countValue.toString()

        plus_btn.setOnClickListener {
            viewModel.plus()
            result_tv.text = viewModel.countValue.toString()
//            countValue++
//            result_tv.text = countValue.toString()
        }

        minus_btn.setOnClickListener {
            viewModel.minus()
            result_tv.text = viewModel.countValue.toString()
//            countValue--
//            result_tv.text = countValue.toString()
        }
    }
}
```

> ### Fragment에서 ViewModel 사용하기

#### TestFragment.kt

```kotlin
package com.woonyum.jetpack_ex

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.FragmentTestBinding

class TestFragment : Fragment() {

    private lateinit var binding: FragmentTestBinding

//    var countValue = 0

    private lateinit var viewModel: TestFragmentViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment

        binding = DataBindingUtil.inflate(inflater, R.layout.fragment_test, container, false)
        viewModel = ViewModelProvider(this).get(TestFragmentViewModel::class.java)
        binding.resultArea.text = viewModel.getCount().toString()

        binding.plus.setOnClickListener {
            viewModel.plus()
            binding.resultArea.text = viewModel.getCount().toString()
//            countValue++
//            binding.resultArea.text = countValue.toString()
        }
        binding.minus.setOnClickListener {
            viewModel.minus()
            binding.resultArea.text = viewModel.getCount().toString()
//            countValue--
//            binding.resultArea.text = countValue.toString()
        }
        return binding.root
    }
}
```

#### TestFragmentViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.ViewModel

class TestFragmentViewModel : ViewModel() {
    var countValue = 0

    fun plus() {
        countValue++
    }

    fun minus() {
        countValue--
    }

    fun getCount(): Int {
        return countValue
    }
}
```

프래그먼트도 액티비티와 똑같이 ViewModel을 사용해줬는데 화면을 회전시키면 값이 0으로 초기화된다.
왜냐하면 프래그먼트는 액티비티에 붙어있기 때문에 액티비티 생명주기의 영향을 받는다. 그래서 액티비티와 같은 방법으로 프래그먼트에 ViewModel을 쓰는 것만으로는 값을 유지할 수 없다. 구글 공식문서에서 말하는 해결법은 `액티비티와 프래그먼트가 뷰모델을 공유하는 것이다.`

<span style="color:#B9B9B9">_구글에서 권장하는 방법은 아니지만 약식으로 아래처럼 액티비티에 해당 코드를 적어서 값의 초기화를 막는 방법도 있다._</span>

#### FragmentActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class FragmentActivity : AppCompatActivity() {

    val manager = supportFragmentManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fragment)

        //구글에서 쓰라한 방법은 아니지만 이렇게 쓰면 화면 전환이 일어날때
        //값이 초기화되지않고 예외처리를 통해 유지될 수 있다
        if (savedInstanceState == null){
            val transaction = manager.beginTransaction()
            val fragment = TestFragment()
            transaction.replace(R.id.frameArea, fragment)
            transaction.addToBackStack(null)
            transaction.commit()
        }


    }
}
```

> ### Activity / Fragment의 ViewModel 공유

공유하는 이유?

1. Activity의 값을 Fragment에서 쓰고 싶거나
2. Fragment에서 값을 ViewModel의 값으로 사용하기 위해서

액티비티와 액티비티 속 프래그먼트(초록색배경)이 ViewModel을 공유하는 예제를 만들었다.
화면 회전 후에도 액티비티와 프래그먼트에 값이 잘 나타나는것을 볼 수 있다.
![](https://velog.velcdn.com/images/woonyumnyum/post/93de543e-98c7-4c17-8ecd-75e32363c76a/image.png)
![](https://velog.velcdn.com/images/woonyumnyum/post/7c718d8d-918a-4db9-9d35-98268ca60875/image.png)

프래그먼트가 액티비티와 ViewModel을 공유하기 위해서는 gradle 파일에 아래 라이브러리를 추가해줘야한다.

#### build.gradle

```kotlin
dependencies {

    // 생략

    implementation 'androidx.fragment:fragment-ktx:1.5.3'
}
```

그리고 ViewModel클래스를 공유할 프래그먼트에서 아래와 같이 viewModel을 액티비티와 같은 ViewModel 클래스로 설정해준다. 이 ViewModel 클래스의 값을 가져와서 text에 적용해주면 화면 회전시 프래그먼트 화면에서도 값이 잘 보존된다. Activity 코드와 ViewModel 코드는 위 예제들과 같다.

#### TestFragment.kt

```kotlin
package com.woonyum.jetpack_ex

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.fragment.app.activityViewModels
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.FragmentTestBinding

class TestFragment : Fragment() {

    private lateinit var binding: FragmentTestBinding
    // ViewModel 클래스 공유
    private val viewModel: MainViewModel by activityViewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        binding = DataBindingUtil.inflate(inflater, R.layout.fragment_test, container, false)
        binding.fragmentText.text = viewModel.getCount().toString()

        return binding.root
    }
}
```

> ### ViewModel Factory

ViewModel Factory를 사용하는 이유?

- Repository 사용하거나 네트워크 통신을 할 때
- 혹은 Local DB를 사용하거나 Room SQLite를 사용할 때

액티비티에서 뷰모델을 생성시 값을 넘겨주고 싶을 때 사용한다.

#### MainViewModelFactory.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider

class MainViewModelFactory(private val num: Int) : ViewModelProvider.Factory {

    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if(modelClass.isAssignableFrom(MainViewModel::class.java)){
            return MainViewModel(num) as T
        }
        throw IllegalArgumentException("UnKnown ViewModel class")
    }

}
```

#### MainViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import android.util.Log
import androidx.lifecycle.ViewModel

class MainViewModel(num: Int) : ViewModel(){

   init{
       Log.d("MainViewModel", num.toString())
   }
}
```

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.lifecycle.ViewModelProvider

class MainActivity : AppCompatActivity() {

    lateinit var viewModel:MainViewModel
    lateinit var viewModelFactory: MainViewModelFactory

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModelFactory = MainViewModelFactory(5000)
        viewModel = ViewModelProvider(this, viewModelFactory).get(MainViewModel::class.java)

    }
}
```

실행하면 액티비티에서 MainViewModel에 넘겨준 값 5000이 잘 출력된 것을 볼 수 있다.
![](https://velog.velcdn.com/images/woonyumnyum/post/5f263959-08ce-4686-9173-2cb4c3f75592/image.png)
