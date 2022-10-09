# Retrofit 사용하기1

## 목차

1. [들어가며](#들어가며)
2. [Retrofit 이란?](#retrofit-이란)
3. [Retrofit 사용해보기](#retrofit-사용해보기)
4. [3번 수정 - 동적으로 데이터 가져오기](#3번-수정---동적으로-데이터-가져오기)

---

<br/>

> ### 들어가며

앱이 데이터소스를 받아오는 대표적인 방법은 Server나 LocalDB에서 데이터를 받아오는 것이다.
Server에서 데이터를 받아올때는 `Retrofit`을 이용하고, LocalDB에서 데이터를 받아올 때는 `ROOM`을 이용한다.

이 과정에서 `코루틴`이라는 개념도 등장한다.
(코루틴은 코틀린뿐만 아니라 파이썬 등 다른 언어에서도 지원한다.)

안드로이드에서 코루틴은 **비동기적으로 실행되는 코드를 간소화하기 위해** 사용할 수 있는 동시 실행 설계 패턴이다.

retrofit을 사용하다보면 콜백이 덕지덕지 붙는 Callback hell 문제점이 생길 수 있다.
이런 콜백 지옥을 코루틴을 통해서 해결할 수 있다.

우리는 앞으로 ViewModel, WorkManager를 코루틴과 함께 사용해볼 예정이다.

---

<br/>

> ### [Retrofit 이란?](https://velog.io/@mingyun12304/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-http-%ED%86%B5%EC%8B%A0Retrofit)

#### Retrofit 이란?

Retrofit 이란 안드로이드에서 서버와 클라이언트 간의 [Http 통신](https://jaejong.tistory.com/40)을 도와주는 라이브러리이다.
초기 안드로이드에서는 서버와의 통신을 위해 HttpClient를 사용했다. 그러나 HttpClien는 Android 5.1 이후로 deprecated 된 후, OKHttp와 그 상위 구현체인 Retrofit을 서버 통신을 위한 라이브러리로 사용된다.

- REST API 통신을 위해 구현되었다.
- OKHttp 라이브러리의 상위 구현체
- retrofit은 OKHttp를 네트워크 계층으로 활용하고 그 위에 구축되었다.

#### 1) Retrofit의 장점

- 빠른 성능
  OKHttp는 AsyncTask를 사용(AsyncTask 보다 3~10배의 성능 차이가 있음)
- 간단한 구현
  반복된 작업을 라이브러리에 넘겨서 처리하므로 간단한 구현이 가능하다.
- 가독성
  Annotation(어노테이션) 사용으로 가독성이 뛰어남.
  동기/비동기 쉬운 구현 - 동기 Synchronous - 동시에 일어난다는 의미로, 요청-응답이 하나의 트랜잭션에서 발생
  요청 후 응답까지 대기한다는 의미 - 비동기 ASynchronous - 동시에 일어나지 않는다는 뜻, 요청-응답은 별개의 트랜잭션
  요청 후 응답이 도착하면 Callback으로 받아침.

#### 2) Retrofit의 구성 요소

- DTO(POJO)
  'Data Transfer Object', 'Plain Old Java Object' 형태의 모델
  JSON 타입변환에 사용
- Interface
  사용할 HTTP CRUD동작(메소드) 들을 정의해놓은 인터페이스
  CRUD -> HTTP Method(POST, GET, PUT, DELETE)
- Retrofit.Builder 클래스
  Interface를 사용할 인스턴스, baseUrl(URL) / Converter(변환기) 설정

---

<br/>

> ### Retrofit 사용해보기

우리는 서버가 따로 없기 때문에 https://jsonplaceholder.typicode.com/
이 사이트에서 제공해주는 무료 API 서버를 이용해서 데이터를 받아와보자.
위 사이트에서 제공하는 posts 데이터 중 첫 번째 데이터를 불러올예정이다. https://jsonplaceholder.typicode.com/posts/1 이 주소로 접속하면 아래와 같은 데이터를 로드할 수 있다.
![](https://velog.velcdn.com/images/woonyumnyum/post/0324af0a-1fb2-46c1-a5a5-b8b14a9c07fa/image.png)

> #### 1-1. 인터넷 권한 설정

#### AndroidManifest.xml

```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

인터넷 사용권한을 허용해준다.

> #### 1-2. gradle 의존성 추가

#### build.gradle

```kotlin
//retrofit 사용
implementation 'com.squareup.retrofit2:retrofit:2.9.0'
implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
```

Retrofit2 라이브러리를 추가해준다.
gson 라이브러리는 Json데이터를 사용자가 정의한 Java 객채로 변환해주는 라이브러리이다.

> #### 2. DTO 모델 클래스 생성

#### Post.kt

```kotlin
package com.woonyum.jetpack_ex

data class Post(
    val userId: Int,
    val id: Int,
    val title: String,
    val body: String
)
```

REST API로 받아올 데이터를 변환하여 매핑할 DTO 클래스 선언 (우리가 받아올 데이터의 틀을 만들어준다고 생각하면 된다.)

**JSON 데이터의 키의 이름과 타입을 일치시켜줘야한다.**
혹은 @SerializedName("속성명")을 이용해서 변수명을 다르게 작성해도된다.

> #### 3. Service 인터페이스 정의

#### MyApi.kt

```kotlin
package com.woonyum.jetpack_ex
import retrofit2.Call
import retrofit2.http.GET

interface MyApi {
    @GET("posts/1")
    fun getPost1():Call<Post>
}
```

HTTP 통신을 위한 서비스 인터페이스를 작성해준다.
네트워크 통신에 이용될 인터페이스로 네트워크 통신이 필요한 순간 호출할 함수를 선언만 한다.
어노테이션을 이용해 HTTP Method를 설정해준다.
(이렇게 HTTP Method를 이용해 통신하는 것을 Restful API라고 한다.)
우리는 데이터를 받아오기 때문에 GET 메소드를 이용해준다.
반환값은 Call 객체이다.

> #### 4. Retrofit 인스턴스 생성

#### RetrofitInstance.kt

```kotlin
package com.woonyum.jetpack_ex

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance {
    val BASE_URL = "https://jsonplaceholder.typicode.com/"

    val client = Retrofit
        .Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getInstance():Retrofit{
        return client
    }
}
```

**Retrofit.Build를 통해 Retrofit 인스턴스 생성**

- baseUrl() 에는 서버의 주소를 넣는데 항상 주소 끝에는 '/'로 끝나야 한다.
- .addConverterFactory()는 데이터를 파싱 할 converter를 추가하는 메서드이다.
  우리는 GsonConverterFactory를 지정하였기 때문에 JSON 데이터를 Gson 라이브러리로 파싱하고 그 데이터를 Model에 자동으로 담아준다.

> #### 5. 통신하기

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

//Simple Retrofit Ex
//https://jsonplaceholder.typicode.com/

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val api = RetrofitInstance.getInstance().create(MyApi::class.java)
        api.getPost1().enqueue(object : Callback<Post>{
            override fun onResponse(call: Call<Post>, response: Response<Post>) {
                Log.d("API1", response.body().toString())
            }

            override fun onFailure(call: Call<Post>, t: Throwable) {
                Log.d("API1", "fail")
            }

        })
    }
}
```

create() 함수로 네트워킹을 위한 Call 객체를 가지는 Service 객체가 자동으로 만들어진다. 이렇게 얻은 Service 객체를 이용해 인터페이스에서 정의한 함수를 호출하면 Call 객체를 얻을 수 있다.

enqueue로 비동기 통신을 실행한다. 통신종료 후 이벤트 처리를 위해 Callback을 등록한다.
onResponse() 함수는 연결에 성공했을 때 실행되고, onFailure는 실패했을때 실행된다.

요청에 성공했을 때 response.body()를 출력해보면 우리가 불러오고자 했던 데이터가 잘 출력되는것을 볼 수 있다.

```
Post(userId=1, id=1, title=sunt aut facere repellat provident occaecati excepturi optio reprehenderit, body=quia et suscipit
    suscipit recusandae consequuntur expedita et cum
    reprehenderit molestiae ut ut quas totam
    nostrum rerum est autem sunt rem eveniet architecto)
```

---

<br/>

> ### 3번 수정 - 동적으로 데이터 가져오기

/posts/1 의 뒤의 숫자를 동적으로 변경해서 다른 posts 데이터를 가져올수있도록 수정해보자.

Service Interface 파일과 MainActivity에서 해당 코드만 수정해주면 된다.

#### MyApi.kt

```kotlin
package com.woonyum.jetpack_ex

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path

interface MyApi {
	//기존 방식
    @GET("posts/1")
    fun getPost1(): Call<Post>

	//동적 방식
    @GET("posts/{number}")
    fun getPostNumber(
        @Path("number") number: Int
    ): Call<Post>
}
```

@GET 어노테이션의 {number} 는 @Path 와 매칭되는 동적인 변수역할을 한다.
만약 number가 1이라면 posts/1 이라는 경로를 나타내며 2라고 하면 posts/2로 변경되어 API를 호출하게 된다.

파라미터에 사용되는 어노테이션의 종류는 다음과 같다.
(출처: https://question0.tistory.com/12)

- @Path - 동적으로 경로를 사용하기 위한 어노테이션
- @Query, @QueryMap - @GET 에서 사용하며 조건 파라미터를 설정
- @Field, @FieldMap - @POST 에서 사용하며 조건 파라미터를 설정
- @Body - 객체를 이용하여 조건 파라미터를 설정
- @Header - 해더 설정

#### MainActivity.kt

```kotlin
package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

//Simple Retrofit Ex
//https://jsonplaceholder.typicode.com/

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val api = RetrofitInstance.getInstance().create(MyApi::class.java)

        //기존 방식
        api.getPost1().enqueue(object : Callback<Post> {
            override fun onResponse(call: Call<Post>, response: Response<Post>) {
                Log.d("API1", response.body().toString())
            }

            override fun onFailure(call: Call<Post>, t: Throwable) {
                Log.d("API1", "fail")
            }

        })

		//동적 방식
        api.getPostNumber(2).enqueue(object : Callback<Post> {
            override fun onResponse(call: Call<Post>, response: Response<Post>) {
                Log.d("API1", response.body().toString())
            }

            override fun onFailure(call: Call<Post>, t: Throwable) {
                Log.d("API1", "fail")
            }
        })
    }
}

```

getPostNumber()의 파라미터로 2를 넘겨주면 posts/2의 데이터에 접근할 수 있다.
getPostNumber(2) 함수를 수행한 결과 response의 body를 출력해보면 posts의 2번 데이터를 성공적으로 받아온 것을 볼 수 있다.

```
Post(userId=1, id=2, title=qui est esse, body=est rerum tempore vitae
    sequi sint nihil reprehenderit dolor beatae ea dolores neque
    fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis
    qui aperiam non debitis possimus qui neque nisi nulla)
```
