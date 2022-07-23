# 배열과 컬렉션

## 목차

1. [배열](#1-배열)
2. [컬렉션](#2-컬렉션)
   <br/>2-1. [리스트](#리스트)
   <br/>2-2. [셋](#셋)
   <br/>2-3. [맵](#맵) <br/>

---

## **<span style="color:#89a5ea">1. 배열</span>**

- 배열(Array)는 원소의 개수를 정해놓고 사용하는 데이터 타입으로, 중간에 개수를 추가하거나 제거할 수 없습니다.
- 배열 객체는 Int, Long, Char 등과 같은 기본 타입 뒤에 Array를 붙여서 만듭니다.

- <예시>

```kotlin
var intArray = IntArray(10)
var longArray = LongArray(10)
var charArray = CharArray(10)
var floatArray = FloatArray(10)
var doubleArray = DoubleArray(10)
```

**문자 배열에 빈공간 할당하기**

- String은 기본 타입이 아니기 때문에 StringArray는 없지만 아래와 같이 사용할 수 있습니다.
- 아래 코드는 10만큼 빈 문자열로 된 배열 공간을 할당합니다.

```kotlin
var stringArray = Array(10, {item->""})
```

**값으로 배열 공간 할당하기**

- arrayOf() 함수를 사용해서 값을 직접 할당할 수도 있습니다.

```kotlin
//String 값 할당하기
var dayArray = arrayOf("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")

//int 값 할당하기
var intArray = intArrayOf(1, 2, 3, 4, 5, 6, 7)
```

**배열에 값 입력하기, 꺼내기**

- 배열에 값 입력하는 방법은 두 가지가 있습니다.

1. 배열명[인덱스] = 값
2. 배열명.set(인덱스, 값)

- 배열의 값을 가져오는 방법은 두 가지가 있습니다.

1. 배열명[인덱스]
2. 배열명.get(인덱스)
   <br/>
   

## **<span style="color:#89a5ea">2. 컬렉션</span>**

- 컬렉션은 배열과는 다르게 공간의 크기를 고정하지 않고 임의의 개수를 담을 수 있습니다.
- 종류 : 리스트, 맵, 셋이 있습니다.
- 코틀린에서 동적으로 컬렉션을 사용하기 위해서는 자료형 앞에 항상 뮤터블(Mutable) 이라는 접두어가 붙습니다.
- ex) mutableList, mutableMap, mutableSet
- 접두어가 없는 이뮤터블(Immutable) 컬렉션도 있지만, 크기와 값을 변경할 수 없게 됩니다. 그래서 add나 set 함수를 지원하지 않고, 최초 입력된 값을 사용만 할 수 있습니다.
- ex) listOf, mapOf, setOf
- 따라서 동적 배열로 사용하기 위해서는 뮤터블로 만들어진 데이터 타입을 사용해야 합니다.

### **<span style="color:#ff8e7f">리스트</span>**

- 저장되는 데이터에 인덱스를 부여하며, 중복된 값을 입력할 수 있습니다.

<br/>

**리스트 생성하기: mutableListOf**

- <예시>

```kotlin
var mutableList = mutableListOf("MON", "TUE", "WED")
```

**리스트에 값 추가하기: add**

- 값이 추가되면서 동적으로 리스트의 공간이 자동으로 증가합니다.
- <예시>

```kotlin
mutableList.add("THU")
```

**리스트 값 가져오기: get**

- mutableList.get(인덱스)

**리스트 값 수정하기: set**

- mutableList.set(인덱스, 값)

**리스트 값 제거하기: removeAt**

- 삭제하면 그 뒤의 인덱스들이 자동으로 앞당겨집니다.
- mutableList.removeAt(인덱스)

**빈 리스트 사용하기**

- mutableListOf<타입>()

### **<span style="color:#ff8e7f">셋<span/>**

- 셋은 중복을 허용하지 않는 리스트입니다.
- 동일한 값은 입력되지 않습니다.
- 인덱스로 조회할 수 없고, get 함수도 지원하지 않습니다.
- String 타입의 값을 입력받기 위해 다음과 같이 선언할 수 있습니다.

```kotlin
//선언
var set = mutableSetOf<String>()
//값 추가하기
set.add("JAN")
set.add("FEB")
set.add("MAR")
//동일한 값은 입력되지 않습니다.
set.add("FEB")
```

**셋의 값 제거하기**

- 셋은 값이 중복되지 않기 때문에 값으로 직접 조회해서 삭제할 수 있습니다.

```kotlin
set.remove("FEB")
```

### **<span style="color:#ff8e7f">맵</span>**

- 맵은 키(key)와 값(value)의 쌍으로 입력되는 컬렉션입니다.
- 제네릭으로 키와 값의 데이터 타입을 지정해서 맵을 생성합니다.
- 키와 값의 타입을 모두 String으로 사용하기 위한 예제입니다.

```kotlin
var map = mutableMapOf<String, String>()
```

**값 추가하기**

- 키와 값을 추가할 때마다 리스트처럼 공간이 늘어납니다.

```kotlin
map.put("키1", "값1")
map.put("키2", "값2")
map.put("키3", "값3")
```

**값 가져오기**

- get() 함수에 키를 직접 입력해서 값을 꺼낼 수 있습니다.

```kotlin
val data = map.get("키1")
```

**맵 수정하기**

- put 함수를 사용할 때 동일한 키를 가진 값이 있으면 키는 유지된 채 그 값만 수정됩니다.

```kotlin
map.put("키2", "수정")
```

**맵 삭제하기**

```kotlin
map.remove("키2")
```
