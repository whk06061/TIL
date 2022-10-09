# Retrofit 사용하기2 (Coroutine + ViewModelScope)

## 목차

1. [동기 방식 vs 비동기 방식](#동기-방식-vs-비동기-방식)
2. [콜백 지옥](#콜백-지옥)
3. [코루틴 사용하기](#코루틴-사용하기)

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

> ### 코루틴 사용하기

코루틴은 비동기적으로 실행되는 코드를 간소화하기 위해 Android에서 사용할 수 있는 동시 실행 설계 패턴이다.
구글은 비동기 프로그래밍에 코루틴을 사용하도록 권장하고 있다.
코루틴은 비동기 처리를 순차적으로 작성할 수 있도록 도와주는 역할을 한다.

그럼 간단하게 코루틴을 사용해보자~

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
        }
        Log.d("TEST", "END")
    }

    suspend fun a(){
        delay(3000)
        Log.d("TEST", "AP1")
    }
}

```

코루틴은 CoroutineScope(Dispatchers.IO).launch로 사용되며 {..}로 묶은 코드가 비동기적으로 실행된다.
실행 결과는 다음과 같다.
![](https://velog.velcdn.com/images/woonyumnyum/post/ff0fd9ac-cda9-4c6d-b7be-4555509a4c48/image.png)
