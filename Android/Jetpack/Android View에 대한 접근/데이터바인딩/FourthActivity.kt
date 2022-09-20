package com.woonyum.jetpack_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class FourthActivity : AppCompatActivity() {
    val manager = supportFragmentManager
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fourth)

        val transaction = manager.beginTransaction()
        val fragment = TestFragment2()
        transaction.add(R.id.frameArea, fragment)
        transaction.commit()
    }
}