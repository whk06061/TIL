지난 코루틴 강의에서 function 앞에 suspend를 붙인다는데 과연 suspend 함수는 무슨 기능을 할까 궁금해서 찾아보았다.
아주 친절하게 설명해주신 [블로그](https://nuritech.tistory.com/16) 발견!

## suspend 단어의 의미
suspend의 사전적 의미는 '중지하다' 이다.
코루틴에서의 suspend 키워드는 시작하고, 멈추고, 다시 시작할 수 있는 함수를 뜻한다고 한다.
- suspend란 비동기 실행을 위한 중단 지점을 의미한다.
- 잠시 중단(suspend)한다는 뜻을 가지고 있고, 즉 잠시 중단 한다면 언젠가 다시 시작(resume)된다는 뜻이다.


## suspend 를 사용하는 이유
하나의 thread가 block될 경우, 해당 thread는 다른 작업을 할 수 없는 block 상태에 놓이게 된다. 즉 block 상태가 풀릴 때 까지 해당 thread는 중지되어 다른 작업을 못한다. 
그러나 suspend function을 사용한다면 block된 상태에 놓일 때, 이 함수를 잠시 suspend 하고 그 기간동안 thread에서 다른 작업을 수행할 수 있다. 완전 효율적이다!

**쉬운 비유**
- 내 하루: 하나의 thread
- 안드로이드 개발을 하다가 build하는데 5분 걸리는 프로젝트를 빌드시킴 -> 5분동안 block 당한 상태
- suspend function의 경우: 빌드가 돌아가는 동안 다른 작업을 한다.
- suspend가 아닌 경우: 빌드가 끝날 때 까지 다른 작업을 못하고 가만히 기다려야 한다.

## 테스트 해보기
suspend 함수를 사용하는 경우와 하지 않을 때 Thread 자원을 어떻게 활용하는지 봐보자. 
- delay() 함수는 suspend 함수로 coroutineScope 안에서만 사용 가능
- Thread.sleep() 함수는 suspend 함수가 아님

#### 테스트1 - suspend function을 사용하지 않은 경우
```kotlin
fun main(){
	 CoroutineScope(Dispatchers.IO).launch {
            //async 이용해 병렬 수행
            async { nonSuspend1() }
            async { nonSuspend2() }
        }
}

fun nonSuspend1(){
        Thread.sleep(3000)
        Log.d(TAG, "{nonSuspend1} After 3s in (${Thread.currentThread().name})")
        Thread.sleep(3000)
        Log.d(TAG, "{nonSuspend1} After 6s in (${Thread.currentThread().name})")

        Log.d(TAG, "{nonSuspend1} END in (${Thread.currentThread().name})")
    }

    fun nonSuspend2(){
        Thread.sleep(1000)
        Log.d(TAG, "{nonSuspend2} After 1s in (${Thread.currentThread().name})")
        Thread.sleep(3000)
        Log.d(TAG, "{nonSuspend2} After 4s in (${Thread.currentThread().name})")

        Log.d(TAG, "{nonSuspend2} END in (${Thread.currentThread().name})")
    }
```
#### 테스트1 결과
![](https://velog.velcdn.com/images/woonyumnyum/post/fc70c697-cd9e-4ecb-a868-3d5e15f9c60a/image.png)
각 함수 nonSuspend1 과 nonSuspend2는 각기 다른 thread 실행됐음을 알 수 있다.
왜냐하면 Thread.sleep() 동안 thread가 block 되어 다른 작업은 수행될 수 없기 때문에, 각 함수는 다른 스레드에서 작동한다.

#### 테스트2 - suspend function을 사용한 경우
```kotlin
fun main(){
	CoroutineScope(Dispatchers.IO).launch {
            suspendTask1()
            suspendTask2()
        }
    }
    
suspend fun suspendTask1() {
        delay(3000)
        Log.d(TAG, "[suspendTask1] After 3s in (${Thread.currentThread().name})")
        delay(3000)
        Log.d(TAG, "[suspendTask1] After 6s in (${Thread.currentThread().name})")

        Log.d(TAG, "[suspendTask1] END in (${Thread.currentThread().name})*****")
    }

suspend fun suspendTask2() {
        delay(1000)
        Log.d(TAG, "[suspendTask2] After 1s in (${Thread.currentThread().name})")
        delay(3000)
        Log.d(TAG, "[suspendTask2] After 4s in (${Thread.currentThread().name})")

        Log.d(TAG, "[suspendTask2] END in (${Thread.currentThread().name}) *****")
    }
```
#### 테스트2 결과
![](https://velog.velcdn.com/images/woonyumnyum/post/ed8ff855-8637-43ce-aa05-ac83d90d5f27/image.png)
Task1과 Task2가 동일한 thread에서 실행되었음을 알 수 있다.
왜냐하면 delay() 동안 thread가 suspend되어 다른 함수의 작업을 수행할 수 있기 때문이다.
(단, suspend 를 사용한다고 무조건 하나의 스레드에서만 실행되는 것은 아니다. 여기서는 2개의 함수(task1, task2) 의 작업(Log.d를 실행하는 것)이 서로 다른 시간에 일어나기 때문에 가능한 것.)



