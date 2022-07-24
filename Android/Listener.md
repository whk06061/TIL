# 리스너

## 리스너 다음에 오는 중괄호 vs 괄호

- 리스너는 인터페이스입니다. 안드로이드는 리스너라는 개념으로 인터페이스를 제공하는데, 인터페이스 안에 개발자가 구현해야 되는 함수의 목록이 미리 정의되어 있습니다.

<br/>

### 레이팅바(Rating Bar)의 리스너

- 예시

```kotlin
public interface OnRatingBarChangeListener {
    void onRatingChanged(RatingBar var1, float var2, boolean var3);
}
```

- 이렇게 정의되어 있는 함수가 1개면 함수명을 작성하지 않고 람다식으로 처리할 수 있습니다.
- 예시

```kotlin
ratingBar.setOnRatingBarChangeListner { ratingBar, rating, fromUser ->
    textView.text = rating.toString()
}
```

<br/>

### 시크바(SeekBar)의 리스너

```kotlin
public interface OnSeekBarChangeListener {
    void onnProgressChanged (SeekBar var1, int var2, boolean var3);
    void onStartTrackingTouch (SeekBar var1);
    void onStopTrackingTouch (SeekBar var1);
}
```

- 함수가 2개 이상이면 괄호를 사용하고 인터페이스에 정의되어 있는 모든 함수를 구현해야 정상적으로 동작합니다.
- 그래서 시크바의 리스너는 괄호를 사용해서, 괄호 안에 오브젝트 형태로 모든 함수를 구현하는 것입니다.
- 함수가 1개인 리스너에 괄호를 사용하는 것도 정상 동작은 하지만 코드가 길어집니다.
- 예시

```kotlin
seekBar.setOnSeekBarChangeListener (object: SeekBar.OnSeekBarChangeListener{
    override fun onnProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean){
        textView.text = progress.toString()
    }

    override fun onStartTrackingTouch(seekBar: SeekBar?){

    }

    override fun onStopTrackingTouch(seekBar: SeekBar?){

    }
})
```
