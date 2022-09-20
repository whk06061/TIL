package com.woonyum.jetpack_ex

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import com.woonyum.jetpack_ex.databinding.FragmentTest2Binding

class TestFragment2 : Fragment() {

    lateinit var  binding : FragmentTest2Binding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = DataBindingUtil.inflate(inflater, R.layout.fragment_test2, container, false)
        binding.fragmentText.text = "변경된 텍스트"
        return binding.root
    }
}