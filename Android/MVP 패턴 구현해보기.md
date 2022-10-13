https://kbw1101.tistory.com/57 이 분의 글을 참고해서 작성했다.

> ## 설계하기

### MVP 적용할 상황 설계

1. 이메일과 이름을 입력하면 로컬 DB에 데이터가 저장된다.
2. 하단 TextView에 저장된 값들이 출력된다.
3. 어플이 재시작될때 저장된 데이터가 있으면 불러와서 TextView에 출력해준다.
   ![](https://velog.velcdn.com/images/woonyumnyum/post/8b4f39db-da43-4ce6-b920-7ff47c0127bb/image.png)

### MVP 구성요소 설계하기

**Model** - 데이터 처리(Local DB에 저장)
**View** - 데이터를 Activity에 출력
**Presenter**: Model과 View의 중재자

<사용자가 View(Activity)에 데이터를 입력하고 저장 버튼 누르면 다음과 같은 Logic이 발생한다.>

(1) View -> Presenter로, 다시 Presenter -> Model로 요청이 넘어간다.
(2) Model에서 데이터를 내부 저장소에 저장하고, Presenter에 View의 갱신을 요청한다.
(3) Presenter에서는 View에 갱신될 데이터를 전달한다.
(4) View에서 갱신될 데이터를 전달받고 출력한다.

<Application이 새롭게 시작될 때 처리되는 Logic은 다음과 같다.>

(1) View -> Presenter로 데이터의 초기화에 대한 요청을 한다.
(2) Presenter에서는 이미 저장된 데이터가 있는지 Model에 요청한다.
(3) Model에서 저장된 데이터가 있는지 확인하고, 이를 Presenter로 전달한다.
(4) Presenter에서는 전달받은 데이터를 View에 넘겨준다.
(5) View에서는 전달받은 데이터가 있다면 View를 갱신하여, 저장된 데이터가 있음을 사용자에게 알린다.

> ## 구현하기

### 레이아웃 파일 작성

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:paddingHorizontal="20dp"
    tools:context=".MainActivity">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="4"
            android:orientation="vertical">

            <EditText
                android:id="@+id/edit_name"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="name" />

            <EditText
                android:id="@+id/edit_email"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:hint="email" />
        </LinearLayout>

        <Button
            android:id="@+id/btn_save"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:text="SAVE" />
    </LinearLayout>

    <TextView
        android:id="@+id/output_name"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="20dp"
        android:textSize="20sp" />

    <TextView
        android:id="@+id/output_email"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="20dp"
        android:textSize="20sp" />
</LinearLayout>
```

### Contractor 작성하기 (View, Presenter 기능 정의하기)

View와 Presenter에 대한 Contractor Interface를 작성한다.

View에서는 다음의 기능을 가져야 한다.

1. 사용자로부터 데이터를 입력받아서 Activity에 출력한다.

Presenter에서는 다음의 기능을 가져야한다.

1. Application이 시작될 때, 저장된 데이터가 있다면 이를 가져온다.
2. 데이터를 TextView에 출력할 수 있도록 View에 데이터 출력을 요청한다.
3. View의 EditText로부터 가져온 데이터를 Model에 저장시킨다.

이를 코드로 작성하면 다음과 같다.

#### Contractor.kt

```kotlin
//View 와 Presenter 기능 정의

interface Contractor {
    interface View {
        fun showInfo(info: JSONObject)  //TextView 에 데이터 출력
    }

    interface Presenter {
        fun initInfo()  //onCreate 될 때, 저장된 데이터가 있으면 화면에 출력
        fun setInfo(info: JSONObject)    //View 한테 TextView 에 데이터 출력하도록 함
        fun saveInfo(info: JSONObject)  //Model 한테 EditText 의 데이터를 저장하도록 함
    }
}
```

### Model 정의하기

```kotlin
//Model 정의하기

interface InfoDataSource {
    interface LoadInfoCallback {
        fun onInfoLoaded(info: JSONObject)
        fun onDataNotAvailable()
    }

    fun getInfo(callback: LoadInfoCallback)
    fun saveInfo(info: JSONObject)
}
```

### Model 구현하기

### InfoRepository.kt

```kotlin
//Model 구현 - View, Presenter 에서는 이 파일을 주입해서 쓴다.

class InfoRepository(context:Context):InfoDataSource {
    private val infoLocalDataSource = InfoLocalDataSource(context)
    override fun getInfo(callback: InfoDataSource.LoadInfoCallback) {
        infoLocalDataSource.getInfo(callback)
    }

    override fun saveInfo(info: JSONObject) {
        infoLocalDataSource.saveInfo(info)
    }

}
```

### InfoLocalDataSource.kt

```kotlin
//Model 구현 - View, Presenter에 주입되는 파일인 InfoRepository 의 코드 복잡성 방지를 위해 이 파일에서 기능 구현.

class InfoLocalDataSource(context: Context) : InfoDataSource {

    //SharedPreferences 는 간단한 데이터를 앱의 개별 저장소에 xml 파일로 저장
    //데이터를 저장할 때는 key/value 형태로 저장
    //SharedPreferences 는 put/get 메소드를 제공하여 데이터를 저장하거나 읽을 수 있음
    private val sharedPreferences = context.getSharedPreferences("info", Context.MODE_PRIVATE)

    //데이터를 저장할 때는 SharedPreferences.Editor 를 통해서 할 수 있습니다.
    //mPreferences.edit()으로 Editor 객체를 가져올 수 있습니다.
    //putString(), putInt() 등의 API 를 통해 데이터를 저장할 수 있습니다.
    private val editor = sharedPreferences.edit()

    override fun getInfo(callback: InfoDataSource.LoadInfoCallback) {
        //SharedPreference 를 통해 값을 가져옴
        var info = sharedPreferences.getString("info", null)
        if (info != null) {
            callback.onInfoLoaded(JSONObject(info))
        }
    }

    override fun saveInfo(info: JSONObject) {
        //SharedPreference 를 통해 데이터 저장
        editor.putString("info", info.toString())
        editor.commit()

    }
}
```

### Presenter 구현하기

```kotlin

//Presenter 구현

class Presenter(val view: Contractor.View, val repository: InfoRepository) : Contractor.Presenter {
    override fun initInfo() {
        //onCreate 될 때, 저장된 데이터가 있으면 화면에 출력
        //Model 아 데이터 가져와
        repository.getInfo(object : InfoDataSource.LoadInfoCallback {
            override fun onInfoLoaded(info: JSONObject) {
                //View 야 화면에 출력해
                view.showInfo(info)
            }

            override fun onDataNotAvailable() {
                //Nothing
            }

        })
    }

    override fun setInfo(info: JSONObject) {
        //View 야 화면에 출력해
        view.showInfo(info)
        Log.d("KBW", info.toString())
    }

    override fun saveInfo(info: JSONObject) {
        // Model 아 저장해
        repository.saveInfo(info)
    }
}
```

### View 구현하기

```kotlin
//View 구현

class MainActivity : AppCompatActivity(), Contractor.View {
    private lateinit var presenter: Contractor.Presenter
    private lateinit var repository: InfoRepository
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //ViewBinding 사용
        binding = ActivityMainBinding.inflate(layoutInflater)
        //Model 주입
        repository = InfoRepository(this)
        //Presenter 주입
        presenter = Presenter(this@MainActivity, repository)
        //앱 시작하면 Presenter 아 화면에 띄워줘
        presenter.initInfo()
        //버튼에 리스너 달아줌
        initButtonListener()

        setContentView(binding.root)
    }

    override fun showInfo(info: JSONObject) {
        binding.outputName.text = info.getString("name")
        binding.outputEmail.text = info.getString("email")

        Log.d("KBW", info.getString("name"))
        Log.d("KBW", info.getString("email"))
    }

    fun initButtonListener(){
        binding.btnSave.setOnClickListener {
            var info = JSONObject()
            info.put("name", binding.editName.text.toString())
            info.put("email", binding.editEmail.text.toString())

            binding.editName.text.clear()
            binding.editEmail.text.clear()

            presenter.setInfo(info)
            presenter.saveInfo(info)
        }
    }

}
```

---
