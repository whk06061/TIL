# Retrofit 사용하기2

## 목차

1. [Retrofit 예제 변경](#retrofit-예제-변경)

> ### Retrofit 예제 변경

[Retrofit 사용하기1](https://velog.io/@woonyumnyum/JETPACK-Retrofit-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0) 에서 작성했던 예제를 코루틴 + 데이터를 화면에 띄우도록 수정해보자.
우선 보기 편하도록 파일들을 package로 묶어줬다.
![](https://velog.velcdn.com/images/woonyumnyum/post/82e3dc75-054a-4cac-a13f-146ecdc16bef/image.png)

#### MyApit.kt

```kotlin
package com.woonyum.jetpack_ex.api

import com.woonyum.jetpack_ex.model.Post
import retrofit2.http.GET
import retrofit2.http.Path

interface MyApi {
    @GET("posts/1")
    suspend fun getPost1():Post

    @GET("posts/{number}")
    suspend fun getPostNumber(
        @Path("number") number: Int
    ): Post
}
```

일반 함수였던 getPost() 함수를 suspend 함수로 바꿔주고 return 타입도 Post로 수정해준다.

#### MainViewModel.kt

MainViewModel 파일을 새로 추가해준다.
그리고 MainActivity에서 수행했던 로직을 MainViewModel로 옮겨준다.

```kotlin
package com.woonyum.jetpack_ex.viewModel

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.woonyum.jetpack_ex.api.MyApi
import com.woonyum.jetpack_ex.api.RetrofitInstance
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {

    private val retrofitInstance = RetrofitInstance.getInstance().create(MyApi::class.java)

    fun getPost1() = viewModelScope.launch {
        val post = retrofitInstance.getPost1()
        Log.d("MainViewModel", post.toString())
    }

    fun getPostNumber(number:Int) = viewModelScope.launch {
        val post = retrofitInstance.getPostNumber(number)
        Log.d("MainViewModel", post.toString())
    }
}
```

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.api.MyApi
import com.woonyum.jetpack_ex.api.RetrofitInstance
import com.woonyum.jetpack_ex.model.Post
import com.woonyum.jetpack_ex.viewModel.MainViewModel
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainActivity : AppCompatActivity() {

    private lateinit var viewModel: MainViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        viewModel = ViewModelProvider(this).get(MainViewModel::class.java)
        viewModel.getPost1()
        viewModel.getPostNumber(3)
        viewModel.getPostNumber(5)
    }

}

```

getPost1() 함수를 실행하면 아래와 같이 데이터 1, 3, 5가 잘 찍히는 것을 볼 수 있다.
![](https://velog.velcdn.com/images/woonyumnyum/post/cb638e72-49dc-461e-8c71-0e1f90b97c24/image.png)
