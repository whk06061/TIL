> # Android의 권장 앱 아키텍처

![](https://velog.velcdn.com/images/woonyumnyum/post/73b69728-7656-4b5f-914e-d10cd83394f9/image.png)
출처:https://developer.android.com/training/dependency-injection/manual?hl=ko

Android의 권장 앱 아키텍처는 코드를 클래스로 분할하여 관심사 분리의 이점을 누리길 권장한다.

지금까지 예제에서는 Repository를 거치지 않고 ViewModel에서 바로 Retrofit으로 데이터를 불러왔었다. 이번 예제에서는 권장 아키텍쳐를 사용하며 Repository를 생성하여 여기서 데이터를 받아오고 ViewModel과 데이터를 연결해서 사용할 것이다.

> # 예제 소개

https://raw.githubusercontent.com/googlecodelabs/kotlin-coroutines/master/advanced-coroutines-codelab/sunflower/src/main/assets/plants.json
Retrofit으로 위 url의 식물 데이터들(텍스트, 이미지)을 불러와서 RecyclerView에 넣어보자
![](https://velog.velcdn.com/images/woonyumnyum/post/ed68667b-b389-4b26-9355-88fc4e762132/image.png)

이번 예제의 패키지 구조는 다음과 같다.
![](https://velog.velcdn.com/images/woonyumnyum/post/28e4f912-ce23-450f-b941-4f429fe9b740/image.png)

---

<br/>

> # 코드로 구현하기

## 1. 종속성을 추가해준다.

#### 1-1. Retrofit, Coroutine, Glide를 사용하기 위해 gradle 파일에 종속성을 추가해준다.

```kotlin
dependencies {
    //retrofit 사용
    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
    implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
    //코루틴 사용
    implementation 'org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.0'
    //ViewModelScope 사용
    implementation 'androidx.lifecycle:lifecycle-viewmodel-ktx:2.4.0'
    //Glide 사용
    implementation 'com.github.bumptech.glide:glide:4.14.2'
    annotationProcessor 'com.github.bumptech.glide:compiler:4.14.2'
}
```

#### 1-2. manifest 파일에서 인터넷 사용을 허가해준다.

```kotlin
<uses-permission android:name="android.permission.INTERNET" />
```

## 2. 데이터 모델(DTO)를 만들어준다.

```kotlin
package com.woonyum.jetpack_ex2.model

data class Plant(
    val plantId: String,
    val name: String,
    val description: String,
    val growZoneNumber: Int,
    val wateringInterval: Int,
    val imageUrl: String
)
```

## 3. Retrofit 객체를 만들어준다.

```kotlin
package com.woonyum.jetpack_ex2.api

object RetrofitInstance {
    val BASE_URL = "https://raw.githubusercontent.com/"

    val client = Retrofit
        .Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getInstance(): Retrofit {
        return client
    }
}
```

## 4. API를 만들어준다.

```kotlin
package com.woonyum.jetpack_ex2.api

interface MyApi {
    @GET("googlecodelabs/kotlin-coroutines/master/advanced-coroutines-codelab/sunflower/src/main/assets/plants.json")
    suspend fun getAllPlants(): List<Plant>
}
```

## 5. Repository 에서 API를 호출해준다.

Repository에서 API를 호출해서 서버로부터 데이터를 받아온다.

```kotlin
package com.woonyum.jetpack_ex2.repository

//서버에서 데이터 가져오는 역할

class Repository {

    private val client = RetrofitInstance.getInstance().create(MyApi::class.java)

    suspend fun getAllData() = client.getAllPlants()
}
```

## 6. ViewModel에서 데이터를 LiveData에 넣어준다.

```kotlin
package com.woonyum.jetpack_ex2.viewModel

class MainViewModel : ViewModel() {

    private val repository = Repository()

    private val _result = MutableLiveData<List<Plant>>()

    val result: LiveData<List<Plant>>
        get() = _result

    fun getAllData() = viewModelScope.launch {
        _result.value =repository.getAllData()
    }
}
```

## 7. 데이터가 받아와지면 RecyclerView에 넣어준다.

```kotlin
package com.woonyum.jetpack_ex2

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val viewModel = ViewModelProvider(this).get(MainViewModel::class.java)
        viewModel.getAllData()
        val rv = findViewById<RecyclerView>(R.id.rv)
        viewModel.result.observe(this, Observer {
            val customAdapter = CustomAdapter(this, it)
            rv.adapter = customAdapter
            rv.layoutManager = LinearLayoutManager(this)
        })
    }
}
```

## 번외. RecyclerView 어댑터 만들기

Glide 라이브러리를 사용해 ImageView에 해당 url 이미지를 넣어준다.

```kotlin
package com.woonyum.jetpack_ex2.adapter

class CustomAdapter(val context: Context, val dataSet: List<Plant>) :
    RecyclerView.Adapter<CustomAdapter.ViewHolder>() {
    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val textView: TextView = view.findViewById(R.id.textArea)
        val imageView: ImageView = view.findViewById(R.id.imageArea)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomAdapter.ViewHolder {
        val view =
            LayoutInflater.from(parent.context).inflate(R.layout.text_row_item, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: CustomAdapter.ViewHolder, position: Int) {
        holder.textView.text = dataSet[position].name
        Glide.with(context)
            .load(dataSet[position].imageUrl)
            .into(holder.imageView)
    }

    override fun getItemCount(): Int {
        return dataSet.size
    }
}
```
