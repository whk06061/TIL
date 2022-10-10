# Retrofit 사용하기2

## 목차

1. [Retrofit 예제 변경](#retrofit-예제-변경)

> ### Retrofit 예제 변경

[Retrofit 사용하기1](https://velog.io/@woonyumnyum/JETPACK-Retrofit-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0) 에서 작성했던 예제를 코루틴으로 변경해보자.
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

함수 앞에 suspend를 붙여주고, return 타입도 Post로 수정해준다.

#### MainViewModel.kt

MainViewModel 파일을 새로 추가해준다.

```kotlin

```
