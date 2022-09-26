> ### 목차

---

1. ViewModel 이란?
2. Activity에서 ViewModel 사용하기
3. Fragment에서 ViewModel 사용하기
4. Activity / Fragment의 ViewModel 공유

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

    private var countValue = 0

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

        result_tv.text = viewModel.getCount().toString()

        plus_btn.setOnClickListener {
            viewModel.plus()
            result_tv.text = viewModel.getCount().toString()
//            countValue++
//            result_tv.text = countValue.toString()
        }

        minus_btn.setOnClickListener {
            viewModel.minus()
            result_tv.text = viewModel.getCount().toString()
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
    private var countValue = 0

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
