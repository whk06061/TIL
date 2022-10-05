LiveData의 값을 변경하는 예제를 만들어보자.
만약 10이 입력되면 첫번째 줄에는 10+10이, 두번째 줄에는 10\*10이 출력되는 예제를 만들어보자.
![](https://velog.velcdn.com/images/woonyumnyum/post/8146c911-74d5-4a86-9543-7168a2dfde25/image.png)

Activity의 observer에서 데이터의 값을 계산해서 출력할 수도 있지만 코드가 복잡해지기 때문에 ViewModel에서 데이터의 값을 변경하도록 했다.

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

ViewModel에서 LiveData의 값을 수정하는 방법은 `Map`을 이용하거나 `SwitchMap`을 이용하면 된다. (둘의 차이점은 나중에 정리하기)
두 함수 모두 LiveData를 리턴한다.

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
