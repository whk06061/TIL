package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class SecondActivity : AppCompatActivity() {
    val manager = supportFragmentManager
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        val transaction = manager.beginTransaction()
        val fragment = TestFragment()
        transaction.add(R.id.frameArea, fragment)
        //transaction.addToBackStack(null)
        transaction.commit()
    }
}