# Coroutine + ViewModelScope 사용하기

## 목차

1. [동기 방식 vs 비동기 방식](#동기-방식-vs-비동기-방식)
2. [콜백 지옥](#콜백-지옥)
3. [코루틴 이란](#코루틴-이란)
4. [코루틴 사용하기](#코루틴-사용하기)
5. [ViewModelScope 사용하기](#viewmodelscope-사용하기)

---

앞 예제에서 차례대로 api.getPostNumber(1), api.getPostNumber(2), api.getPostNumber(3), api.getPostNumber(4) 를 호출하면 차례대로 posts/1, 2, 3, 4 데이터가 불러와질 것 같지만 실제로 실행해보면 순서가 뒤죽박죽이다.
왜냐하면 Retrofit은 `비동기적`으로 데이터를 불러오기 때문이다.

> ### 동기 방식 vs 비동기 방식

- 동기 방식은 서버에서 요청을 보냈을 때 응답이 돌아와야 다음 동작을 수행할 수 있다. 즉 A작업이 모두 진행 될때까지 B작업은 대기해야한다.
- 비동기 방식은 반대로 요청을 보냈을 때 응답 상태와 상관없이 다음 동작을 수행 할 수 있다. 즉 A작업이 시작하면 동시에 B작업이 실행된다. A작업은 결과값이 나오는대로 출력된다.

그러나 만약 함수들이 순차적으로 실행이 되어야 한다면 아주 간단한 방법으로 구현할 수 있다.

> ### 콜백 지옥

```kotlin
api.getPostNumber(1).enqueue(object : Callback<Post> {
         override fun onResponse(call: Call<Post>, response: Response<Post>) {
             api.getPostNumber(2).enqueue(object : Callback<Post> {
                 override fun onResponse(call: Call<Post>, response: Response<Post>) {
                     api.getPostNumber(3).enqueue(object : Callback<Post> {
                         override fun onResponse(call: Call<Post>, response: Response<Post>) {
                         }

                         override fun onFailure(call: Call<Post>, t: Throwable) {
                         }
                     })
                 }

                 override fun onFailure(call: Call<Post>, t: Throwable) {
                 }
             })
         }

            override fun onFailure(call: Call<Post>, t: Throwable) {
            }
        })
```

이 코드처럼 1번 데이터 응답을 받았을때 2번 데이터 불러오는 함수를 호출하도록 코드를 작성하면 함수가 순차적으로 실행될 수 있다.
그러나 콜백이 덕지덕지 붙으면서 코드가 엄청 복잡해지고 `콜백 지옥`에 빠지는 것을 볼 수 있다.

콜백지옥을 해결하기 위해 등장한 것이 바로 **코루틴**이다!

> ### 코루틴 이란

코루틴(Coroutines) 은 쓰레드(Thread)와 기능적으로는 비슷하지만, 하나의 쓰레드 내에서 여러 개의 코루틴이 실행되는 개념으로 비동기 프로그래밍에 권장되는 동시 실행 설계 패턴이다.

코루틴은 단일 쓰레드 내에서 여러 개의 코루틴을 실행할 수 있기 때문에, 많은 양의 동시 작업을 처리할 수 있으면서 메모리 절약의 장점이 있다.

이유는, 기존 쓰레드는 Context-Switching(CPU가 쓰레드를 점유하면서 실행, 종료를 반복하며 메모리 소모)이 발생하기 때문에 많은 양의 쓰레드를 갖기가 어렵지만

반면에 코루틴은 쓰레드가 아닌 루틴을 일시 중단(suspend) 하는 방식이라 Context-Switching에 비용이 들지 않기 때문이다.

또한, 지정된 작업 범위 내에서 실행이 되기 때문에 메모리 누수를 방지할 수 있다.

즉, 코루틴은 쓰레드의 간소화된 버전이라고 할 수 있다.

### 코루틴 vs 스레드

스레드의 경우 자원경쟁, 데드락 등의 문제가 많지만, 코루틴은 별도의 스레드 없이 메인 스레드 상에서 번갈아가며 병렬처리와 유사한 동작을 수행할 수 있다.

스레드는 비동기로, 여러 스레드가 있으면 동시에 실행되는 반면, 코루틴은 이전에 진행중이던 루틴은 정지된다. 즉, 한번에 하나의 코드만 실행된다.

그럼 간단하게 코루틴을 사용해보자~

> ### 코루틴 사용하기

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

//간단한 Coroutine + ViewModelScope
//https://jsonplaceholder.typicode.com/

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("TEST", "START")
        CoroutineScope(Dispatchers.IO).launch {
            a()
            b()
        }
        Log.d("TEST", "END")
    }

    suspend fun a(){
        delay(3000)
        Log.d("TEST", "AP1")
    }
    suspend fun b(){
        delay(1000)
        Log.d("TEST", "BP1")
    }
}
```

코루틴은 CoroutineScope(Dispatchers.IO).launch로 사용되며 {..}로 묶은 코드가 비동기적으로 실행된다.
AP1은 3초 후 출력되고, BP1은 1초 후 출력되므로
START -> END -> BP1 -> AP1 순으로 로그에 찍힐 것 같지만
실행 결과는 다음과 같다.
![](https://velog.velcdn.com/images/woonyumnyum/post/4b14da22-d311-4745-b4f3-cf07856ee121/image.png)
즉 코루틴 안에 쓴 함수들은 순차적으로 실행된다는 것을 알 수 있다!
(헷갈리면 안되는 점이 CoroutineScope(Dispatchers.IO).launch{..} 으로 묶은 함수는 비동기적으로 실행되기 때문에 START -> END가 먼저 실행된다. 순차적으로 실행되는 것은 {..} 내부에서의 일이다!)

> ### ViewModelScope 사용하기

ViewModel에서 코루틴을 실행하는 예제를 만들어보자.
MainActivity에서 버튼을 누르면 SecondActivity로 이동하고, SecondViewModel(SecondActivity와 연결됨)에서 for문 안에서 1초 딜레이 후 숫자를 찍는 코루틴 코드를 작성해보자.

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

//간단한 Coroutine + ViewModelScope
//https://jsonplaceholder.typicode.com/

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.goToSecond).setOnClickListener {
            val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)
        }
    }
}
```

#### SecondViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import android.util.Log
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class SecondViewModel : ViewModel() {
    //뷰모델에서 비동기작업을 해보자
    fun a() {
        CoroutineScope(Dispatchers.IO).launch {
            for (i in 0..10) {
                delay(1000)
                Log.d("SecondViewModel", i.toString())
            }
        }
    }
}
```

#### SecondActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider

class SecondActivity : AppCompatActivity() {
    lateinit var viewModel: SecondViewModel
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        viewModel = ViewModelProvider(this).get(SecondViewModel::class.java)
        viewModel.a()
    }
}
```

MainActivity에서 버튼을 누르면 SecondActivity로 이동하고 for문이 출력된다. 그러나 뒤로가기를 통해 SecondActivity에서 벗어나도 SecondViewModel에서 코루틴이 종료되지 않고 계속 실행되는 것을 볼 수 있다. 그래서 액티비티에서 벗어나서 뷰모델이 필요가 없어질때 코루틴이 종료되게 하려면 별도로 처리를 해야한다. 이는 매우 번거로운 작업이다.

이럴때 [ViewModelScope](#https://developer.android.com/topic/libraries/architecture/coroutines?hl=ko)를 사용하면 간편하게 코루틴을 처리할 수 있다.

> #### build.gradle 종속성 추가

```kotlin
implementation 'androidx.lifecycle:lifecycle-viewmodel-ktx:2.4.0'
```

> #### SecondViewMoel에서 viewModelScope 사용하기

#### SecondViewModel.kt

```kotlin
package com.woonyum.jetpack_ex

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class SecondViewModel : ViewModel() {
    //뷰모델에서 비동기작업을 해보자
    fun a() {
        CoroutineScope(Dispatchers.IO).launch {
            for (i in 0..10) {
                delay(1000)
                Log.d("SecondViewModel A:", i.toString())
            }
        }
    }

	//viewModelScope 사용하기
    fun b(){
        viewModelScope.launch {
            for (i in 0..10) {
                delay(1000)
                Log.d("SecondViewModel B:", i.toString())
            }
        }
    }
}
```

#### SecondActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider

class SecondActivity : AppCompatActivity() {
    lateinit var viewModel: SecondViewModel
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        viewModel = ViewModelProvider(this).get(SecondViewModel::class.java)
        viewModel.a()
        viewModel.b()
    }
}
```

SecondViewModel 에서 함수 b는 viewModelScope를 사용해서 for문을 돌면서 숫자를 출력한다. SecondActivity를 벗어나면 viewModelScope를 사용한 b는 더이상 출력되지 않고 a만 출력되는 것을 볼 수 있다.
