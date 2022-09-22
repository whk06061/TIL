package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.databinding.DataBindingUtil
import com.woonyum.jetpack_ex.databinding.ActivityMainBinding

//DataBinding
//데이터 결합

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    var testCount = 20

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)

        //기존의 방법
        //binding.tvName.text = "바뀐 텍스트"

        //기존의 방법과 다르게 데이터 결합을 할 수는 없을까?
        //데이터 결합
        val person = Person("개복치", 20)
        binding.user = person

    }

    fun myClick(view: View){
        testCount++
        //데이터 결합
        val person = Person("개복치", testCount)
        binding.user = person
    }
}